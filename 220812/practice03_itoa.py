def atoi(ss):
    res = '' # 결과값 담을 빈 문자열
    minus = '' # 마이너스 일 경우 추가할 문자열
    
    if ss == 0: # 0일 경우, 바로 내보냄
        return chr(48)
    while ss:
        if ss > 0: # 양수일 경우
            a, b = divmod(ss, 10) #divmod로 값과 나머지 뽑아냄
            i = chr(b+48) # 나머지 값
            res = i + res # 나머지 값 결과값 앞에 붙이기
            ss = a # 몫을 다시 전체값으로
        else:
            ss = ss * -1 # 양수로 만듦
            minus = '-' # 마이너스 붙이기

    return minus + res

res = atoi(int(input()))
print(res, type(res))   
