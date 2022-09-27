def 순열(i,k,total):
    global min_mx
    if i == k:
        x = sum(p)
        if x < min_mx:
            min_mx = x
    elif total > min_mx:
        return
    else:
        for j in range(k):
            if used[j] == 0:     # a[j] 가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 사용됨으로 표시
                p[i] = field[i][j]     # p[i]는 a[j]로 결정
                순열(i+1, k, total+p[i])       # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제   

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    p = [0] * N
    min_mx = 1000000000
    순열(0,N,0)
    print(f'#{tc} {min_mx}')

