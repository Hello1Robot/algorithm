T = 10 # 테스트케이스 갯수
for test_case in range(1, T+1):
    N = int(input()) # 테스트케이스 번호
    ob = input() # 찾을 문자
    st = input() # 대상 문자열
    res = st.split(ob) # 문자로 자르기

    print(f'#{test_case} {len(res)-1}') # 결과값-1 출력


