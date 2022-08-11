T = int(input())

for test_case in range(1, T+1):
    field = [[0]*10 for _ in range(10)]
    # (2,2) (4,4)가 주어진다면 색칠해야 하는 범위는
    # (4-2), (4-2)니까 x가 2~4, y가 2~4인 범위이다.
    # 두 번째 x좌표-첫 번째 x좌표 = x값
    # 두 번째 y좌표 - 첫 번째 y 좌표 = y값

    # 문제에서 주지 않는 것 : 첫번째 좌표보다 두 번째 좌표가 항상 값이 큰가?
    # 스웨아 멍청한놈들...

    aria = int(input())
    quest = []
    for _ in range(aria):
        questn = list(map(int, input().split()))
        quest.append(questn)
    cnt = 0
    for qu in quest:
        for i in range(qu[0], qu[2]+1):
            for j in range(qu[1], qu[3]+1):
                if field[i][j] != qu[4]:
                    field[i][j] += qu[4]
                if field[i][j] == 3:
                    cnt += 1
    print(f'#{test_case} {cnt}')
    