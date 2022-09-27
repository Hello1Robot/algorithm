def 순열(i,k,total):
    global res_max
    if i == k:
        if total > res_max:
            res_max = total
        return
    elif total <= res_max:
        return
    else:
        for j in range(k):
            if used[j] == 0:    
                used[j] = 1    
                p[i] = field[i][j]/100     
                순열(i+1, k, total*p[i])       
                used[j] = 0    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    
    field = [list(map(float,input().split())) for _ in range(N)]
    used = [0] * N
    p = [0] * N
    res_max = 0
    순열(0,N,1)
    print(f'#{tc} {res_max*100:6f}')