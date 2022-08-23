for test_case in range(1,11):
    길이 = int(input())
    N = list(input())
    nums = list(map(str, range(10)))
    res = [] # 숫자 들어오면 넣을 리스트
    stk = [] # 연산자 넣을 스택

    for n in N:
        if n in nums: # 숫자면 res에 넣기
            res.append(n)
        elif n == '(':
            stk.append(n)
        elif n == '+': # 연산자일 경우 스택을 확인. +의 경우 순위가 낮아서 다 수행해야됨
            while stk:
                if stk[-1] == '(':
                    break
                else:
                    x = stk.pop()
                    if x == '+':  # 더하기 경우, 뒤에서 두개 뽑아서 계산하고 집어넣기
                        a = res.pop()
                        b = res.pop()
                        c = int(a)+int(b)
                        res.append(str(c))
                    elif x == '*': # 곱하기도 뒤에서 두 개 뽑아서 계산하고 집어넣기
                        a = res.pop()
                        b = res.pop()
                        c = int(a)*int(b)
                        res.append(str(c))                    
            stk.append(n)
        elif n == '*': # 위와 동일.
            while stk:
                if stk[-1] == '+' or stk[-1] == '(': # +보다는 순위가 높으니까 +는 통과
                    break
                else:
                    stk.pop()
                    a = res.pop()
                    b = res.pop()
                    c = int(a)*int(b)
                    res.append(str(c))  
            stk.append(n)
        elif n == ')':
            while stk:
                x = stk.pop()
                if x == '(':
                    break
                elif x == '*':
                    a = res.pop()
                    b = res.pop()
                    c = int(a)*int(b)
                    res.append(str(c))
                elif x == '+':
                    a = res.pop()
                    b = res.pop()
                    c = int(a)+int(b)
                    res.append(str(c))                                        
    while stk: # 남은 스택이 없을 때까지 계산반복
        x = stk.pop()
        if x == '+':
            a = res.pop()
            b = res.pop()
            c = int(a)+int(b)
            res.append(str(c))
        elif x == '*':
            a = res.pop()
            b = res.pop()
            c = int(a)*int(b)
            res.append(str(c))
    
    print(f'#{test_case} {res[0]}')