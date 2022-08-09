T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_val = min_val = nums[0]

    for i in range(1,N):
        if nums[i] > max_val:
            max_val = nums[i]
        if nums[i] < min_val:
            min_val = nums[i]
    res = max_val - min_val
    print(f'#{test_case} res')