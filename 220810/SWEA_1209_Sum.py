import sys
sys.stdin = open("1209.txt")

T = 10

for test_case in range(1, T+1):
    field = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    crs1 = 0
    crs2 = 0

    for i in range(100): # 가로 합 구하기 (쉬움)
        ss = sum(field[i])
        if ss > max_sum:
            max_sum = ss
    
    for x in range(100): # 세로 합 및 대각선 합 구하기
        ss = 0
        for y in range(100):
            ss += field[x][y]
            if x == y:
                crs1 += field[x][y]
            if x + y == 99:
                crs2 += field[x][y]
        if ss > max_sum:
            max_sum = ss
    
    print(f'{test_case} {max(max_sum, crs1, crs2)}')
    