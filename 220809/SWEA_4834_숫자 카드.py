T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = list(input())
    num_list = [0] * 10
    res_list = []
    for num in numbers:
        num_list[int(num)] += 1
    for idx, i in enumerate(num_list):
        res_list.append((i, idx))
    res_list.sort()
    print(f'#{test_case} {res_list[-1][1]} {res_list[-1][0]}')