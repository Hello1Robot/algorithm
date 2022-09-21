def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, I+1)

A = list(range(1,6))
n = len(A)
r = 3
comb = [0] * r
nCr(n,r,0)