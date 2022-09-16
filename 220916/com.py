a = [2,1,1,4] #  원재료
group = set()
# 조합
def comb(n,m,j): # [1, 2, 3, 4]
    if n == m:
        print(chosen)
        return
    else:
        for i in range(j, len(a)):
            chosen[n] = a[i]            # n 자리에 뽑은 후 입력
            comb(n+1, m, i+1)           # n+1 자리로 이동, 인덱스는 그 이후 생각

m = 2                                   # 2개 뽑기
chosen = [-1] * m                       # 조합을 만들 저장소 [-1, -1]
comb(0,2,0)