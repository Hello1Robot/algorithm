def DFS(start):
    stk = []
    stk.append(start)
    visited[start] = 1
    while stk:
        x = stk.pop()
        for i in range(1,N+1):
            if field[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stk.append(i)
    return True

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    field = [[0]*(N+1) for _ in range(N+1)]
    root = list(map(int,input().split()))
    for i in range(0,len(root),2):
        field[root[i]][root[i+1]] = 1
        field[root[i+1]][root[i]] = 1
    cnt = 0
    visited = [0]*(N+1)
    for i in range(1,N+1):
        if visited[i] == 0:
            cnt += DFS(i)
    
    print(f'#{tc} {cnt}')
    # 그냥 몇 덩이인지 구하는 거 아니야?
