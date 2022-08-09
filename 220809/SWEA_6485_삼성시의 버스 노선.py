T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A_list = []
    B_list = []
    for _ in range(N):
        a, b = map(int, input().split())
        A_list.append(a)
        B_list.append(b)
    P = int(input())
    num_list = []
    bus_dict = dict()
    for _ in range(P):
        x = int(input())
        num_list.append(x)
        bus_dict[x] = 0

    for i in range(N):
        for j in range(A_list[i], B_list[i]+1):
            if j in bus_dict.keys():
                bus_dict[j] += 1
    print(f'#{test_case}', end=' ')

    for n in num_list:
        print(bus_dict[n], end=" ")
    print()