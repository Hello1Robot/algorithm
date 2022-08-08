N = int(input())
nums = list(map(int, input().split()))

max_num = nums[0]
for i in range(1,N):
    if nums[i] > max_num:
        max_num = nums[i]

a = nums.index(max_num)
b = nums.index(max_num, a+1, N-1)
max_gap = b-a

print(max_gap)