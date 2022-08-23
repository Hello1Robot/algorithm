T = int(input())
for test_case in range(1,T+1):
    N = list(input())
    nums = list(map(str,range(10)))
    stk=[]
    print(f'#{test_case} ', end='')
    for n in N:
        if n in nums:
            print(n, end='')
        else:
            stk.append(n)

    while stk:
        print(stk.pop(), end='')
    print()