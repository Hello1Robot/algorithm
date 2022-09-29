# visited에 값을 넣어놓고
# 만약 현재값보다 갱신된 값이 작을 때만 갱신

import heapq
def dijkstra(x,y):
    heap = []
    heapq.heappush(heap, (0,x,y))
    visited[x][y] = 0
    while heap:
        cost, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if field[nx][ny] > field[x][y]:
                new_cost = cost + field[nx][ny]-field[x][y] + 1
            else:
                new_cost = cost + 1
            if visited[nx][ny] > new_cost:
                visited[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))
                


dx = [0,1,0,-1]
dy = [1,0,-1,0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(map(int,input().split())) for _ in range(N)]
    visited = [[999999]*N for _ in range(N)]
    print(f'#{tc} {dijkstra(0, 0)}')