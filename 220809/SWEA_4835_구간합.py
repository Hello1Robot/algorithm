T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    case = list(map(int, input().split()))
    minV = 999999999
    maxV = 0
    for i in range((N-M)+1):
        sum1 = 0
        for j in range(M):
            sum1 += case[i+j]
        if sum1 > maxV:
            maxV = sum1
        if sum1 < minV:
            minV = sum1

    print(f'#{test_case} {maxV-minV}')