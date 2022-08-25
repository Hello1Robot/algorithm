from collections import deque

def bfs(start, end):
    que = deque()
    que.append(start)
    while que:
        x,y = que.popleft()
        for i in range(4): # 네 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 도로이고 방문한 적 없을 경우
            if 0 <= nx < 16 and 0 <= ny < 16 and field[nx][ny] == 0 and visited[nx][ny] == False:
                que.append((nx,ny)) # 큐에 값 추가
                visited[nx][ny] = True # 방문으로 처리
            elif 0 <= nx < 16 and 0 <= ny < 16 and field[nx][ny] == 3: # 목적지 도착
                # 도착했으니까 1 리턴
                return 1
    # 도착 못할 경우 0 리턴
    return 0        
        
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for test_case in range(1,11):
    N = int(input())
    # 길이는 16으로 고정
    field = [list(map(int,input())) for _ in range(16)] # 필드 생성
    visited = [[False]*16 for _ in range(16)] # 방문여부 확인하는 필드
    stt_x = stt_y = 0
    end_x = end_y = 0
    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                stt_x = i
                stt_y = j
            elif field[i][j] == 3:
                end_x = i
                end_y = j
    
    print(f'#{test_case} {bfs((stt_x,stt_y),(end_x,end_y))}')
    