from collections import deque

def bfs(start,end,cnt):
    que = deque()
    que.append((start,end, cnt))
    global flag # 깃발 펄럭펄럭
    while que and flag:
        start, end, cnt = que.popleft() # 시작/끝/카운트
        if start == end: # 끝점 도달시
            flag = False
            return cnt # 카운트값 리턴
        for i in range(1,N+1):
            # 노드가 이어져 있고 방문한 적이 없을 경우
            if field[start][i] == 1 and visited[i] == False:
                # 큐에 더해주고, 카운트 1 증가시켜줌 
                que.append((i, end, cnt+1))
                visited[i] = True
    return 0
        

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    field = [[0]*(N+1) for _ in range(N+1)] # 노드 담아줄 필드
    visited = [False]*(N+1) # 방문사실 기록
    flag = True
    for i in range(M):
        a, b = map(int,input().split())
        # 양방향 노드니까, 대칭되는 점도 이어줌
        field[a][b] = 1
        field[b][a] = 1
    
    start, end = map(int,input().split()) # 탐색하고자 하는 시작점 , 끝점 받기
    print(f'#{test_case} {bfs(start,end,0)}')