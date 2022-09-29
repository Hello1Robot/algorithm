def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    root = list(map(int,input().split()))
    rep = [i for i in range(N+1)]

    for i in range(0,len(root),2):
        u, v = root[i], root[i+1]
        union(u,v)
    cnt = 0

    for i in range(1,N+1):
        if i == rep[i]:
            cnt += 1
    print(f'#{tc} {cnt}')

