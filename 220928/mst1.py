def mst1(r,V):
    MST = [0]*(V+1) # MST 포함 여부
    key = [10000]*(V+1) # 가중치의 최대값 ㅇㅇ




V, E = map(int,input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    adjM[u][v] = w
    adjM[v][u] = w # 가중치가 있는 무방향 그래프
    adjL[u].append((v,w))
    adjL[v].append((u,w))