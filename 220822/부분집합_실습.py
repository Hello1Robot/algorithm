def f(i, N):
    global cnt
    if i == N:
        a = sum(bit)
        if a == 10:
            cnt += 1
    else:
        bit[i] = A[i] # 포함여부만을 bit에 나타냄
        f(i+1, N)
        bit[i] = 0
        f(i+1,N)

A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * 10
cnt = 0
f(0,10)
print(cnt)