T = int(input())

for test_case in range(1, T+1):
    str1 = list(input()) # 찾을 오브젝트
    str2 = list(input()) # 비교할 문자열
    len1 = len(str1) # 둘 다 리스트화
    len2 = len(str2)
    ans = 0 # 없으면 0 있으면 1
    for i in range(len2-len1+1):
        cnt = 0
        for j in range(len1):
            if str1[j] == str2[i+j]:
                cnt += 1
        if cnt == len1: # 길이만큼 일치하면 정답있음
            ans = 1
            break
    print(f'#{test_case} {ans}')