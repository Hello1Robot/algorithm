T = int(input())

for test_case in range(1, T+1):
    rstA = list(input())
    A_set = set(rstA) # 중복되는 문자 제거
    A_dict = {key:0 for key in A_set} # dict로 해서 카운트
    rstB = list(input())
    for n in rstB: # for문 돌리면서 dict에 값 추가
        if n in A_dict:
            A_dict[n] += 1
    res = max(A_dict.values()) # 최대값 뽑기
    print(f'#{test_case} {res}')