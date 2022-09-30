from collections import deque
# 상(0) 하(1) 좌(2) 우 (3)
# 수학적인 그래프이기 때문에 가로와 세로를 바꾸어 생각해야함
# 진짜 화나...
# 그냥 y,x 순서로 해야될듯?ㅎ
# 상 : y증가 하 : y감소 좌 : x 감소 우 : x 증가
dx = [1,-1,0,0]
dy = [0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cell_cnt = N
    total = 0
    field = [[0]*4001 for _ in range(4001)]
    # 좌표값이 음수도 나오니까, 고려해서 필드 생성
    # 이러면, 이제 들어오는 좌표값에 1000을 더해서 입력해주면 됨
    # 시뮬레이션 진행하면서 같은 레벨에서 만나면 펑!
    que = deque()
    for _ in range(N):
        y, x, forward, energy = map(int,input().split())
        y = (y+1000)*2
        x = (x+1000)*2
        field[x][y] = [0,energy,False]
        que.append((x,y,0,forward,energy))
    
    while que and cell_cnt:
        x, y, level, forward, energy = que.popleft()
        if field[x][y] == 0 or field[x][y][2]:
            continue
        nx = x + dx[forward]
        ny = y + dy[forward]
        if nx > 4000 or nx < 0 or ny > 4000 or ny < 0:
            cell_cnt -= 1
            continue
        if field[nx][ny] == 0:
            field[nx][ny] = [level+1, energy,False]
            field[x][y] = 0
            que.append((nx,ny,level+1,forward,energy))
        else:
            if not field[nx][ny][2]:
                if field[nx][ny][0] == level+1:
                    field[nx][ny][2] = True
                    field[x][y] = 0
                    total += field[nx][ny][1] + energy
                    cell_cnt -= 2
            else:
                if field[nx][ny][0] == level+1:
                    field[x][y] = 0
                    total += energy
                    cell_cnt -= 1
                else:
                    field[nx][ny] = [level+1, energy, False]
                    field[x][y] = 0
                    que.append((nx,ny,level+1,forward,energy))

    print(f'#{tc} {total}')
