T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    DP = [0] * (N+1)

    for q in range(1,Q+1):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            DP[i] = q
    
    DP.pop(0)
    print(f'#{test_case}', end=' ')
    for dp in DP:
        print(dp, end=' ')
    print()