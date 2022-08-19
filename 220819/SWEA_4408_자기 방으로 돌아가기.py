# 최대 시간만 구하는 거니까
# 겹치는 게 몇 개나 있는지만 확인하면 됨
# 결국 좌표 확인하는 문제라고 생각
# 시작좌표, 끝좌표가 나오니까.
# 좌표값을 튜플로 생각
# (10,20) (30,40) (50,60) (70,80) 이런 식으로.
# 겹치는 걸 어떻게 확인할 지 생각해봐야지.
# 그냥 저 사이의 범위를 카운팅하는 걸로 하자.
# 400개의 방이 있는 리스트를 하나 만들자.
T = int(input())
for test_case in range(1, T+1):
    rooms = [0] * 201

    N = int(input())
    for _ in range(N):
        a, b = map(int,input().split())
        if a % 2:
            a = a//2 + 1
        else:
            a = a // 2
        
        if b % 2:
            b = b//2 + 1
        else:
            b = b // 2
        
        if a > b:
            a,b = b,a
        
        for i in range(a, b+1):
            rooms[i] += 1
    
    print(f'#{test_case} {max(rooms)}')