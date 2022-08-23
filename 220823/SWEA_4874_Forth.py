T = int(input())

for test_case in range(1,T+1):
    nums = input().split()
    stk = []
    for n in nums:
        if n.isdecimal():
            stk.append(int(n))
        elif n == '.':
            if len(stk) == 1:
                print(f'#{test_case} {stk[0]}')
            else:
                print(f'#{test_case} error')
        else:
            if len(stk) < 2:
                print(f'#{test_case} error')
                break
            if n == '/':
                b = stk.pop()
                a = stk.pop()
                c = a / b
                stk.append(c)
            elif n == '*':
                b = stk.pop()
                a = stk.pop()
                c = a * b
                stk.append(c)
            elif n == '+':
                b = stk.pop()
                a = stk.pop()
                c = a + b
                stk.append(c)
            elif n == '-':
                b = stk.pop()
                a = stk.pop()
                c = a - b
                stk.append(c)
