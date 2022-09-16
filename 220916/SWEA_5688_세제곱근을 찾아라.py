T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 큰 값 찾기
    R = round(N**(1/3)) # 세제곱근 찾기. 근사값 고려해서 round
    
    if R**3 == N: # 세제곱과 같으면 (즉 정수)
        print(f'#{test_case} {R}')
    else: # 정수가 아니면
        print(f'#{test_case} -1')