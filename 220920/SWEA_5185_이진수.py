T = int(input())
for test_case in range(1,T+1):
    n, st = input().split()
    rst = list(st)
    rs = ''
    for num in rst:
        n = format(int(num, 16), '04b')
        rs = rs + n
    print(f'#{test_case} {rs}')
    

    