from collections import deque
def BFS(x=0, y=0):
    global min_res
    que = deque()
    visited[x][y] = 0
    que.append((x,y))
    while que:
        x,y = que.popleft()
        if x == N-1 and y == N-1:
            if min_res > visited[x][y]:
                min_res = visited[x][y]
        elif min_res <= visited[x][y]:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if field[nx][ny] > field[x][y]:
                new_cost = visited[x][y] + field[nx][ny]-field[x][y]+1
            else:
                new_cost = visited[x][y] + 1
            if visited[nx][ny] > new_cost:
                visited[nx][ny] = new_cost
                que.append((nx,ny))
    

dx = [0,1,0,-1]
dy = [1,0,-1,0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(map(int,input().split())) for _ in range(N)]
    visited = [[99999999]*N for _ in range(N)]
    min_res = 99999999
    BFS()
    print(f'#{tc} {min_res}')
