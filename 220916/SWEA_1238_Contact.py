# 비상연락망 문제
# BFS 돌면서 레벨 체크하고
# 레벨 가장 높은 것 중 가장 큰 값 뽑기
from collections import deque

def 너비우선탐색(start,cnt):
    que = deque()
    que.append((start,cnt))
    visited[start] = 1
    while que:
        start, cnt = que.popleft()
        for x in range(1,101):
            if field[start][x] == 1 and not visited[x]:
                visited[x] = 1
                check_list.append((cnt, x))
                que.append((x,cnt+1))


for test_case in range(1,11):
    N, start = map(int,input().split())
    field = [[0]*101 for _ in range(101)]
    visited = [0]*101
    check_list = []
    data = list(map(int,input().split()))
    for i in range(0,N,2):
        field[data[i]][data[i+1]] = 1
    너비우선탐색(start, 1)
    check_list.sort()
    print(f'#{test_case} {check_list[-1][1]}')
    
    # 숫자 카운트까지 해서 bfs 돌리면 될듯
    
    