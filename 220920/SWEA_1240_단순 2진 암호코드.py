# pwd = {'0001101':'0','0011001':'1','0010011':'2','0111101':'3','0100011':'4','0110001':'5','0101111':'6','0111011':'7','0110111':'8','0001011':'9'}
pwd = {'1011000':'0','1001100':'1','1100100':'2','1011110':'3','1100010':'4','1000110':'5','1111010':'6','1101110':'7','1110110':'8','1101000':'9'}
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    rst = []
    for _ in range(N):
        st = list(map(int,input()))
        if sum(st) == 0:
            continue
        else:
            if not rst:
                st.reverse()
                rst.append(st)
    rst = list(map(str, rst[0]))
    cnt = 0
    odd = 0
    even = 0
    start = rst.index('1')
    while start < len(rst)-5:
        pw = ''.join(rst[start:start+7])

        if pw in pwd.keys():
            if cnt % 2:
                odd += int(pwd[pw])
            else:
                even += int(pwd[pw])
            cnt += 1
            start += 6
        else:
            start += 1

    if ((odd*3)+even) % 10:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {even+odd}')