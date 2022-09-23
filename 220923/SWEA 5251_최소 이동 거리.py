import heapq
def 다이크스트라(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for node, cst in field[now]:
            cost = dist + cst
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(que, (cost, node))

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    distance = [100000000]*(N+1)
    field = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        start, end, cs = map(int,input().split())
        field[start].append((end, cs))
    
    다이크스트라(0)
    print(f'#{tc} {distance[N]}')