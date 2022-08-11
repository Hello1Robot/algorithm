T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    res = []

    print(f'#{test_case}', end=' ')
    while len(res) != 10:
        res.append(nums.pop())
        res.append(nums.pop(0))
    print(*res)