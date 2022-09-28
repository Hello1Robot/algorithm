# DFS로 구현해보기
def dfs(x,y):
    stk = []
    stk.append((x,y))
    visited[x][y] = field[x][y]
    while stk:
        x,y = stk.pop()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= N:
                continue
            if visited[nx][ny] > visited[x][y] + field[nx][ny]:
                stk.append((nx,ny))
                visited[nx][ny] = visited[x][y] + field[nx][ny]

T = int(input())
dx = [1,0]
dy = [0,1]
for tc in range(1,T+1):
    N = int(input())
    field = [list(map(int,input().split())) for _ in range(N)]
    visited = [[10000]*N for _ in range(N)]
    dfs(0,0)
    print(f'#{tc} {visited[N-1][N-1]}')