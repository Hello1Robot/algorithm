def f(i, N):
    if i == N:
        print(bit)
    else:
        bit[i] = A[i]
        f(i+1, N)
        bit[i] = 0
        f(i+1,N)

A = [1,2,3]
bit = [0] * 3
f(0,3)