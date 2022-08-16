# 기본적으로 완전탐색으로 A에 B에 해당하는 문자열이 몇 개 있는지를 찾는다.
# 찾으면 찾은 갯수만큼 len(A) - B*n + n 을 출력한다.

T = int(input())
for test_case in range(1, T+1):
    N, M = input().split()
    rst1 = list(N)
    rst2 = list(M)
    l1 = len(rst1)
    l2 = len(rst2)
    res_cnt = 0 # 바꿀 수 있는 게 몇 개인지 세는 카운트
    len_cnt = 0 # while문 종료조건
    while len_cnt < (l1-l2+1): # for문과 동일한 범위
        cnt = 0
        for j in range(l2):
            if rst1[len_cnt+j] == rst2[j]:
                cnt += 1
        if cnt == l2: # 같은 갯수가 M의 길이라면
            res_cnt += 1 # 결과카운트 +1
            len_cnt += (l2-1) # 검사지점 끝으로 이동
        len_cnt += 1

    res = l1 - (l2*res_cnt) + res_cnt # 결과값 계산
    print(f'#{test_case} {res}') # 출력