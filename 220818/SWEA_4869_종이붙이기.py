T = int(input())
for test_case in range(1, T+1):
    N = int(input())//10
    DP = [0]*(N+1)
    DP[1] = 1
    for i in range(2, N+1):
        if i % 2:
            DP[i] = (DP[i-1] * 2) -1
        else:
            DP[i] = (DP[i-1]*2) +1
    print(f'#{test_case} {DP[N]}')