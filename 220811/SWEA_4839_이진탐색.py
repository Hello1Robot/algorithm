# 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 
# 중간 페이지 c= int((l+r)/2)

def check_book(x, y):
    l = 1
    c = 0
    cnt = 0
    while c != y:
        c = (l+x)//2
        if c > y:
            x = c
        else:
            l = c
        cnt += 1
    return cnt

T = int(input())

for test_case in range(1, T+1):
    page, pa, pb = map(int, input().split())
    A_result = check_book(page, pa)
    B_result = check_book(page, pb)
    if A_result > B_result :
        print(f'#{test_case} B')
    elif A_result < B_result:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')