# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
T = int(input())

for test_case in range(1, T+1):
    arr = list(range(1,13))
    N = 12
    cnt = 0

    # 원소 수, 목표 값
    A, B = map(int,input().split())
    for i in range(1, 1<<N):
        rst = []
        for j in range(N):
            if i & (1<<j):
                rst.append(arr[j])
        if len(rst) == A and sum(rst) == B:
            cnt += 1
    
    if cnt :
        print(f'#{test_case} {cnt}')
    else:
        print(f'#{test_case} 0')
