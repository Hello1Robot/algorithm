def dfs(start):
    dfs_list.append(start)
    for y in range(len(graph[start])):
        if graph[start][y] == 1 and (y not in dfs_list):
            dfs(y)
T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())

    graph = [[0] * (N+1) for _ in range(N + 1)]
    dfs_list = []
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1

    stt, point = map(int,input().split())
    res = 0
    dfs(stt)
    if point in dfs_list:
        res = 1
    print(f'#{test_case} {res}')