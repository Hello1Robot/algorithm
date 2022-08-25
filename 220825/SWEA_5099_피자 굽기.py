from collections import deque

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split()) # 화덕크기 / 피자 수 받기
    pizzzza = list(map(int,input().split()))
    for idx, val in enumerate(pizzzza): # 피자번호를 위해 enumerate
        pizzzza[idx] = [val, idx+1]

    pizzza = deque(pizzzza)
    gama = deque()
    res = []
    for x in range(N):
        gama.append(pizzza.popleft()) # 화덕에 휫자 집어넣기
    while gama: # 가마에 피자 있을 때
        gama[0][0] = gama[0][0] // 2 # 한바퀴 돌아서 치즈가 뜨끈뜨끈해지면 치즈가 반으로 줄어듦
        if gama[0][0] == 0: # 치즈 다 녹았으면
            if pizzza: # 대기하는 피자가 있을 때
                gama[0] = pizzza.popleft() # 대기하는 피자를 넣어줌
            else: # 없다면
                res.append(gama.popleft()) # 뜨끈뜨끈한 피자 꺼내서 손님한테 내어줌
                continue # 팝 해서 자리 비었는데 지 알아서 채워짐

        gama.rotate(-1) # 만약 0이 아니라면, 화덕 이동
 
    print(f'#{test_case} {res[-1][1]}') # 마지막 휫자의 인덱스번호 출력

