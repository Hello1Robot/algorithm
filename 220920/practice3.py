T = int(input())
pwd = {'001101':'0', '010011':'1','111011':'2','110001':'3','100011':'4','110111':'5','001011':'6','111101':'7','011001':'8','101111':'9'}

for _ in range(T):
    st = input()
    N = int(st, 16)
    output = ''
    for j in range(len(st)*4 -1, -1, -1):
        output += "1" if N & (1 << j) else "0"
    rst = list(output)
    goal = len(rst)
    cnt = 0
    while cnt < goal-5:
        a = ''.join(rst[cnt:cnt+6])
        if a in pwd.keys():
            print(pwd[a], end=' ')
            cnt += 6
        else:
            cnt += 1
    print()
