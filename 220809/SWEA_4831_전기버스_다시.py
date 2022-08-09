import sys

sys.stdin = open('4831.txt')

T = int(input())

for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    # K : 한 번 충전으로 이동할 수 있는 거리
    # N : 종점의 위치
    # M : 충전기가 설치된 수
    field = [0] * (N+1) # 충전소 위치를 담을 리스트 초기화
    chargers = list(map(int, input().split())) # 충전소 받아옴
    cnt = 0
    for c in chargers: # 충전소를 필드에 넣음
        field[c] = 1
    field.pop(0) # 충전소 첫번째 칸에서 출발하므로, 첫번째 칸을 없애줌
    charger_list = [] # 지나온 충전소를 담을 리스트
    while len(field) > K: # 필드 끝까지 갈 때 까지 반복
        for i in range(K): # K만큼 가면서, 충전소가 있는 인덱스를 확인
            if field[i] == 1:
                charger_list.append(i) # 충전소가 있는 인덱스를 charger_list에 담기
        if len(charger_list) == 0: # 만약 차저리스트가 비어있으면
            cnt = 0 # 카운트를 0으로 만들고 브레이크
            break
        else: # 차저리스트에 값이 들어있으면
            field = field[charger_list[-1]+1:] # 리스트의 맨 뒤의 값까지 필드를 자르기.
						# 맨 뒤의 값까지 잘라야 하니, 시작부는 맨 뒤 + 1 이 된다.
            charger_list.clear() # 충전하고 새로운 여정을 떠나야 하는 관계로, 충전소리스트 초기화
            cnt += 1 # 충전했으니까 카운트 올리기
    print(f'#{test_case} {cnt}')