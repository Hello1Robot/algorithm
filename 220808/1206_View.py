T = 10

for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(nums)-2):
        max_left = nums[i-2]
        if nums[i-1] > max_left:
            max_left = nums[i-1]
        max_right = nums[i + 2]
        if nums[i + 1] > max_right:
            max_right = nums[i + 1]
        if nums[i] > max_left and nums[i] > max_right:
            a = nums[i] - max_left
            b = nums[i] - max_right
            gap = a
            if b < gap:
                gap = b
            cnt += gap
    print(f'#{test_case} {cnt}')

