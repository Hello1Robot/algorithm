def f(i,N,s,t): # 인덱스, 원하는 길이, 합, 최종 값
    if i == N: 
        if s == t:
            res = list(filter(None, bit))
            print(res)
    else:
        bit[i] = A[i]
        f(i+1,N,s+A[i],t)
        bit[i] = 0
        f(i+1,N,s,t)

A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*10
f(0,10,0,10)