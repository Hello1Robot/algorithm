from collections import deque
def merge_sort(rst):
    if len(rst) == 1:
        return rst
    
    left = []
    right = []
    middle = len(rst) // 2
    for x in rst[:middle]:
        left.append(x)
    for x in rst[middle:]:
        right.append(x)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    global cnt
    result = []
    left = deque(left)
    right = deque(right)
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right)> 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif len(left) > 0:
            result.append(left.popleft())
        elif len(right) > 0:
            result.append(right.popleft())

    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rst = list(map(int,input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(rst)[N//2]} {cnt}')

