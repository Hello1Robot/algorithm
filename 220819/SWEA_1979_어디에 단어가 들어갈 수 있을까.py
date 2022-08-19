T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(map(int,input().split())) for _ in range(N)]
    res = 0
    # 가로 줄 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if field[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    res += 1
                cnt = 0
        if cnt == K:
            res += 1
    # 세로 줄 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if field[j][i]:
                cnt += 1
            else:
                if cnt == K:
                    res += 1
                cnt = 0
        if cnt == K:
            res += 1
    print(f'#{test_case} {res}')