# 생각 먼저 하자.
# N*N개의 리스트를 0으로 초기화
# 0,0에 1을 부여하고, y값 상승
# 다음 y값이 범위 밖이거나 0이 아니면, 방향 바꾸기
# 그럼 방향을 생각해보면, 오른쪽 - 아래 - 왼쪽 - 위 니까


T = int(input())

for test_case in range(1, T+1):
    # 방향설정 : 오른쪽 아래 왼쪽 위
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    N = int(input())
    field = [([0]*N) for _ in range(N)]
    cnt = 1 # 값 + 종료포인트
    idx = 0 # 방향값 설정하는 인덱스
    field[0][0] = 1 # 첫번째 필드 미리 설정
    x = 0 # 기본 x 값 설정
    y = 0 # 기본 y 값 설정
    while cnt < N*N: # 종료값은 N의 제곱값
        nx = x + dx[(idx%4)] # 다음으로 이동할 x값
        ny = y + dy[(idx%4)] # 다음으로 이동할 y값
        if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위를 벗어난 값일 때 방향 변경
            idx += 1
            continue
        if field[nx][ny] != 0: # 이미 다른 값이 들어 있을 때 방향 변경
            idx += 1
            continue
        cnt += 1
        field[nx][ny] = cnt
        x = nx
        y = ny
    
    print(f'#{test_case}')
    for n in field:
        print(*n)