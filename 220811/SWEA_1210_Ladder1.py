import sys
sys.stdin = open("1210.txt")

def ladder(start):
    x = 0
    y = start

    while x != 99:
        if 0 <= y-1 and field[x][y-1] != 0: # 왼쪽 가능한지 확인. 가능하면
            while True:
                y -= 1
                if y >= 0:
                    if field[x][y] == 0:
                        y += 1
                        x += 1
                        break
                else:
                    y += 1
                    x += 1
                    break
        elif y+1 < 100 and field[x][y+1] != 0: # 오른쪽 가능한지 확인. 가능하면
            while True:
                y += 1
                if y < 100:
                    if field[x][y] == 0:
                        y -= 1
                        x += 1
                        break
                else:
                    y -= 1
                    x += 1
                    break
        else:
            x += 1
    return y



for test_case in range(1, 11):
    numb = int(input())
    field = []
    for _ in range(100):
        mapp = list(map(int, input().split()))
        field.append(mapp)
    field = field[::-1]
    start = field[0].index(2)
    print(f'#{test_case} {ladder(start)}')





