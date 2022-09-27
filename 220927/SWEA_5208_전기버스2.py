T = int(input())
for tc in range(1,T+1):
    N, *rst = map(int,input().split())
    rst = rst + ([0]*100)
    val = rst[0]
    cnt = 0
    idx= 0
    while idx < N-1:
        비교값 = 0
        이동값 = 0
        for i in range(1,val+1): # 이러면 밸류가 1,2이 나오겠네?
            # (val-idx)
            if (rst[i+idx]-(val-i)) >= 비교값:
                비교값 = (rst[i+idx]-(val-i))
                이동값 = i
        cnt += 1
        idx += 이동값

        val = rst[idx]
        if idx + val >= N-1:
            break
    print(f'#{tc} {cnt}')