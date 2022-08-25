from collections import deque

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split()) # 숫자 갯수, 회전 수 받기
    nums = list(map(int,input().split())) # 숫자들 받아오기
    que = deque(nums) # 리스트 큐 선언
    que.rotate(-M) # 로테이트로 회전시키기
    print(f'#{test_case} {que.popleft()}') # 맨 앞 뽑아서 출력