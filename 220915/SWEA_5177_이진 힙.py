import heapq
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    rst = list(map(int,input().split()))
    que = []
    for rs in rst:
        heapq.heappush(que, rs)

    tot = 0
    i = N//2
    while i:
        tot += que[i-1]
        i = i // 2

    
    print(f'#{test_case} {tot}')