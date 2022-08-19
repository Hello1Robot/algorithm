T = int(input())
for test_case in range(1,T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    # 그냥 sum으로 확인. 45인지
    sdoku2 = list(zip(*sdoku))
    res = 1
    cnt = 0
    for i in range(9):
        if sum(sdoku[i]) == 45 and sum(sdoku2[i]) == 45:
            cnt +=1
            continue
        else:
            res = 0
            break
    if res:
        for i in range(0,7,3):
            cube = 0
            for j in range(0,7,3):
                cube += sdoku[i][j]+sdoku[i+1][j]+sdoku[i+2][j]
                cube += sdoku[i][j+1]+sdoku[i+1][j+1]+sdoku[i+2][j+1]
                cube += sdoku[i][j+2]+sdoku[i+1][j+2]+sdoku[i+2][j+2]
                if cube == 45:
                    cube = 0

                else:
                    res = 0
                    break
    print(f'#{test_case} {res}')
    