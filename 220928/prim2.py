def prim2(r,V):
    MST = [0]*(V+1) # MST 포함 여부
    MST[r] = 1
    s = 0

    for _ in range(V): #V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s




V, E = map(int,input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    adjM[u][v] = w
    adjM[v][u] = w # 가중치가 있는 무방향 그래프

print(prim2(0,V))