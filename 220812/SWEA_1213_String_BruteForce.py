#각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 찾을 문자열, 그 다음 줄에는 검색할 문장
T = 10
for test_case in range(T):
    N = int(input()) # 테스트케이스의 번호
    q = list(input()) # 찾을 문자열
    ob = list(input()) # 검색할 문장
    res_count = 0 # 결과값
    for i in range(len(ob)-len(q)+1): 
        ok = True
        for j in range(len(q)): # 전체를 찾으면서, 같지 않으면 False로
            if q[j] != ob[i+j]:
                ok = False
        if ok: # 전체값이 같은 문장만 True로 받음
            res_count += 1
    print(f'#{N} {res_count}')