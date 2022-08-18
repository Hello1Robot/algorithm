def dfs(start):
    dfs_list.append(start)
    for y in range(len(graph[start])):
        if graph[start][y] == 1 and (y not in dfs_list):
            dfs(y)

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N + 1)]
dfs_list = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(V)
print(*dfs_list)