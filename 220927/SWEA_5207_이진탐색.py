def 이진탐색(s,e,q):
    right_flag = 0
    left_flag = 0
    while s <= e:
        if right_flag > 1 or left_flag > 1:
            return False
        mid = (s+e)//2
        if A[mid] > q:
            e = mid-1
            left_flag += 1
            right_flag = 0
            continue
        elif A[mid] < q:
            s = mid+1
            right_flag += 1
            left_flag = 0
            continue
        elif A[mid] == q:
            return True
    return False


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    res = 0
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    for b in B:
        res += 이진탐색(0,N-1,b)
    
    print(f'#{tc} {res}')