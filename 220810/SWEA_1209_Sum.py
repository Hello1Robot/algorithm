import sys


sys.stdin = open("1209.txt")


T = 10


for test_case in range(1, T+1):

    N = input()

    field = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    crs1 = 0

    crs2 = 0

    for x in range(100):  # 세로 합 및 대각선 합 구하기
        s1 = 0

        s2 = 0

        for y in range(100):

            s1 += field[x][y]

            s2 += field[y][x]

            if x == y:

                crs1 += field[x][y]

            if x + y == 99:

                crs2 += field[x][y]

        if s1 > max_sum:

            max_sum = s1

        if s2 > max_sum:

            max_sum = s2

    print(f'#{test_case} {max(max_sum, crs1, crs2)}')
