from collections import deque

def BFS(start): # BFS 시작
    que = deque() # 덱 선언
    que.append(start) # 덱에 시작지점 넣기 
    global flag # 도착여부를 알려주는 변수
    cnt = 1 # 가는 데 걸린 시간
    while que and flag == 0: # 큐에 변수가 들어있고, 도착하지 않았을 경우
        x,y,c = que.popleft() # x좌표 y좌표 카운트 꺼내기
        for i in range(4): # 네 방향 확인하기
            nx = x + dx[i] 
            ny = y + dy[i]
            # 범위 내인지, 길인지, 방문했는지 확인
            if 0 <= nx < N and 0 <= ny < N  and field[nx][ny] == 0 and visited[nx][ny] == 0:
                que.append((nx,ny,c+1)) # 방문안했으니 큐에 넣기
                visited[nx][ny] = 1 # 방문한다고 표시
                field[nx][ny] = 1 # 길 도착했으니 막기(안해도 됨)

            # 만약 3을 찾았으면, 그동안의 카운트값을 적어보냄
            elif 0 <= nx < N and 0<=ny<N and field[nx][ny] == 3:
                flag = c

T = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for test_case in range(1,T+1):
    N = int(input())
    x = y = 0
    flag = 0 # 도착 여부를 나타내는 변수 선언
    # 미로 만들기
    field = [list(map(int,input())) for _ in range(N)]
    # 방문여부 확인하는 필드 만들기
    visited = [[0]*N for _ in range(N)]

    # 시작 지점 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 2:
                x = i
                y = j
                break
    BFS((x,y,0)) #BFS 실행 (BTS 아님)
    print(f'#{test_case} {flag}') # 결과값 출력
    