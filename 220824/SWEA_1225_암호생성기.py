from collections import deque
# % 5 를 쓰면 좀 맛있게 풀 수 있을 듯
T = 10
for test_case in range(1,T+1):
    case = int(input()) # 케이스. 필요없음
    nums = list(map(int,input().split())) # 숫자 9개 받기
    que = deque(nums) # 큐 선언
    cnt = 0 # 뺄 카운트값
    while que[-1] > 0:
        A = que.popleft() # 왼쪽 꺼 빼옴
        que.append(A-(cnt%5+1)) # cnt만큼 빼줌
        cnt += 1 # 카운트 더해줌
    
    que[-1] = 0 # 마지막 값 0으로 바꾸기
    print(f'#{test_case}', end=' ')
    print(*que)