T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)] # field를 만드는데, str은 처리하기 힘드니까 리스트화시키기
    res = '' # 결과값 담을 빈 str
    odd = '' # 홀수일 때 가운데값 넣을 빈 str
    for i in range(N):
        for j in range(N-M+1):
            cnt1 = 0 # 가로 카운트
            cnt2 = 0 # 세로 카운트
            half1 = '' # 가로 절반
            half2 = '' # 세로 절반
            for x in range(M//2):
                # 가로세로 돌며 비교
                if field[i][j+x] == field[i][j+(M-x-1)]:
                    cnt1 += 1
                    half1 += field[i][j+x]
                if field[j+x][i] == field[j+(M-x-1)][i]:
                    cnt2 += 1
                    half2 += field[j+x][i]   
                # 가로값 카운트 & 세로값 카운트가 비교한 숫자와 일치하면 res            
            if cnt1 == M//2:
                if M % 2:
                    odd += field[i][j+x+1]
                res = half1 + odd + half1[::-1]
                break
            if cnt2 == M//2:
                if M % 2:
                    odd += field[j+x+1][i]
                res = half2 + odd + half2[::-1]
                break            

    print(f'#{test_case} {res}')