T = int(input())

for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    # K : 한 번 충전으로 이동할 수 있는 거리
    # N : 종점의 위치
    # M : 충전기가 설치된 수
    chargers = list(map(int, input().split()))
    chargers.append(N)
    total = K
    cnt = 0
    for i in range(len(chargers)-1):
        if total >= chargers[i+1]:
            pass
        elif total >= chargers[i]:
            total = K + chargers[i]
            cnt += 1
        else:
            cnt = 0
            break
    if total < N:
        cnt = 0

    print(f'#{test_case} {cnt}')

    