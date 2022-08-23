def f(i,N,s,t): # 인덱스, 원하는 길이, 합, 최종 값
    if s >= t: # 만약 총합이 목표값보다 같거나 크면 종료
        if s == t: # 부분집합의 합이 목표치일 경우
            res = list(filter(None, bit)) # 0인 값 제거
            print(res) # 프린트
            return
    elif i == N:
        return
    else:
        bit[i] = A[i]
        f(i+1,N,s+A[i],t)
        bit[i] = 0
        f(i+1,N,s,t)

A = [1,2,3,4,5,6,7,8,9,10]
bit = [0]*10
f(0,10,0,10)