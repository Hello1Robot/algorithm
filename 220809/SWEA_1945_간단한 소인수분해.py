T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    res_list = []
    nums = [2, 3, 5, 7, 11]
    num_count = 0
    for i in nums:
        while N % i == 0:
            N = N // i
            num_count += 1
        res_list.append(num_count)
        num_count = 0
    print(f'#{test_case}', end=" ")
    print(*res_list)