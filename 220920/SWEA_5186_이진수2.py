T = int(input())
for test_case in range(1,T+1):
    N = float(input())
    res = ''
    cnt = 0
    while N:
        N *= 2
        정수 = int(N)
        N = N - 정수
        res =  res + str(정수)
        cnt += 1
        if cnt >= 13:
            res = 'overflow'
            break
    print(f'#{test_case} {res}')