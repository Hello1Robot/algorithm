# 괄호의 짝이 맞는지를 검사
T = int(input())
for test_case in range(1, T+1):
    qu = list(input())
    stack_list = []
    for q in qu:
        if q == '(':
            stack_list.append(q)
        elif q==')':
            if stack_list:
                stack_list.pop()
            else:
                stack_list.append(q)
                break
    print(stack_list)
    if stack_list:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} 1')