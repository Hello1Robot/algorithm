from collections import deque

def Bfs(start):
    que = deque()
    que.append(start)
    while que:
        x = que.popleft()
        if x not in bfs_list:
            bfs_list.append(x)
            print(x, end='-')
            for i in range(N+1):
                if field[x][i] == 1 and i not in bfs_list:
                    que.append(i)

N, M = map(int,input().split())

field = [[0]*(N+1) for _ in range(N+1)]
nodes = list(map(int,input().split()))
bfs_list = []
for i in range(0,len(nodes),2):
    x, y = nodes[i], nodes[i+1]
    field[x][y] = 1
    field[y][x] = 1

Bfs(1)
print()
