# 필드 전체에 BFS를 돌면서 맥스값 찾기
# 만약 같은 값이 들어온다면 작은 값 넣기
# 맨 뒤의 값 출력하기

from collections import deque

def 너비우선탐색(x,y,cnt):
    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if field[nx][ny] == field[x][y] + 1:
                cnt += 1 
                que.append((nx,ny))
                break
    return cnt
        



dx = [-1,1,0,0] # 델타 설정
dy = [0,0,-1,1]

T = int(input())

for test_case in range(1,T+1):
    N = int(input()) # N 받기
    field = [list(map(int,input().split())) for _ in range(N)] # 필드 만들기
    max_cnt = 0
    cnt_list = []
    for i in range(N):
        for j in range(N):
            ct = 너비우선탐색(i, j, 1)
            if ct > max_cnt:
                max_cnt = ct
                cnt_list.append((field[i][j], ct))
            elif ct == max_cnt:
                if field[i][j] < cnt_list[-1][0]:
                    cnt_list.append((field[i][j], ct))

    print(f'#{test_case} {cnt_list[-1][0]} {cnt_list[-1][1]}')