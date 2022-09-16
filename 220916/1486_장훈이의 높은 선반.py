def 부분집합(i, N, a, T):
    global min_cnt
    if a >= T:
        if a < min_cnt:
            min_cnt = a
        return
    if i == N:
        return
    
    else:
        bit[i] = staff[i]
        부분집합(i+1, N, a+staff[i], T)
        bit[i] = 0
        부분집합(i+1, N, a, T)

T = int(input())
for test_case in range(1,T+1):
    N, B = map(int,input().split())
    staff = list(map(int,input().split()))
    bit = [0]*N
    min_cnt = 1000000000
    부분집합(0,N,0,B)
    print(f'#{test_case} {min_cnt-B}')
    