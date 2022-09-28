def prim1(r,V):
    MST = [0]*(V+1) # MST 포함 여부
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결되는 데 드는 비용
    key[r] = 0 # 시작 정점의 key
    for _ in range(V): #V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
            MST[u] = 1      # 정점 u를 MST에 추가
            # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key) # MST 가중치의 합




V, E = map(int,input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    adjM[u][v] = w
    adjM[v][u] = w # 가중치가 있는 무방향 그래프

prim1(0,V)