# 합인뎅... 합인뎅... 합인뎅...

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    DP = [[] for _ in range(N+1)]
    DP[0].append(1)
    DP[1].extend([1,1])
    for i in range(2,N):
        DP[i].append(1)
        for j in range(len(DP[i-1])-1):
            DP[i].append(DP[i-1][j]+DP[i-1][j+1])
        DP[i].append(1)
    DP.pop()
    print(f'#{test_case}')
    for dp in DP:
        print(*dp)