T = int(input())
for test_case in range(1,T+1):
    st = list(input())
    stak = []
    res_cnt = 0
    for s in st:
        if s == '{':
            stak.append(s)
        elif s == '}':
            if not stak:
                break
            else:
                a = stak.pop()
                if a != '{':
                    break
        elif s == '(':
            stak.append(s)
        elif s == ')':
            if not stak:
                break
            else:
                a = stak.pop()
                if a != '(':
                    break
    else:
        if not stak:
            res_cnt = 1
    print(f'#{test_case} {res_cnt}')