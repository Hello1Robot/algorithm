T = int(input())

# 모르겠다. 스터디 하고 다시 풀어봄
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    cnt = 0
    for i in range(1<<N):
        for j in range(N):
            sum_list = 0
            sum_count = 0
            if i & (1<<j):
                sum_list += arr[j]
                sum_count += 1
            print(sum_list)
        if sum_list == 0 and sum_count != 0:
            cnt += 1
    if cnt:
        print(1)
    else:
        print(0)