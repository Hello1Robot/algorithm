from collections import deque
def BFS(start, end):
    que = deque()
    visited = [0]*1000001
    que.append(start)
    visited[start] = 1
    while que:
        x = que.popleft()
        if x == end:
            return visited[x]-1
        if x+1 <= 1000000 and visited[x+1] == 0:
            visited[x+1] = visited[x]+1
            que.append(x+1)
        if x-1 >=0 and visited[x-1] == 0:
            visited[x-1] = visited[x]+1
            que.append(x-1)
        if x*2 <= 1000000 and visited[x*2] == 0:
            visited[x*2] = visited[x]+1
            que.append(x*2)
        if x-10 >= 0 and visited[x-10] == 0:
            visited[x-10] = visited[x]+1
            que.append(x-10)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    print(f'#{tc} {BFS(N,M)}')