T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split()) # 값 받아오기
    a, b = divmod(N,K) # 몫과 나머지로 나누기
    if b == 0: # 나누어 떨어질 경우
        print(f'#{test_case} {a**K}') # 몫을 K제곱한 게 값
    else: # 떨어지지 않을 경우
        res = 1
        for i in range(b): # 나머지의 수만큼 a에 1을 더해주고 제곱
            res *= (a+1)
        for j in range(K-b): # K에서 남은 값만큼 다시 제곱
            res *= a
        print(f'#{test_case} {res}')