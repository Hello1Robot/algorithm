# 1, 2, 3, 4 버블 버블
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    for i in range(N, 0, -1):
        for j in range(i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(f'#{test_case}', end=' ')
    for n in nums:
        print(n, end=' ')
    print()