from collections import deque
# 아이디어 정리하기
# for 문으로 루프를 돌면서, 각 지점에서 함수 실행
# 각 함수는 아래쪽 대각선에 있는 값을 넣으면서 돔
# 함수의 i값을 이용해서 방향 설정 - i의 값에 따라서 탐색할 방향 변경
# 만약 이미 탐색된 값을 발견 시 break
# 아닐 시 방향을 바꿔서 계속 탐색
# ↙↘↗↖ 순으로 탐색.
def BFS(a,b,i): # 탐색을 위해 BFS 함수 설정, 시작 x,y좌표와 이동방향
    global max_cnt # 최대값 찾을 맥스 카운트 설정
    que = deque()
    que.append((a,b,i,field[a][b].zfill(3))) 
    # zfill 설명. zfill 은 자릿수를 설정하는 함수
    # 입력되는 숫자는 1부터 100까지 3자리
    # visited와 같은 리스트 대신 str을 쓰는데,
    # 한자리를 그대로 넣으면 '11'같은 값이 들어가 있을 때 '1'이 들어가지 못하는 문제가 발생
    # 그래서 001, 011 와 같은 형식으로 넣고 비교.
    
    while que:
        x, y, i, vis = que.popleft()
        nx = x + dx[i%4]
        ny = y + dy[i%4]
        if nx >= N or nx < 0 or ny >= N or ny < 0 : # 범위 넘으면 탈출
            continue
        if nx == a and ny == b:                     # 만약 처음 값으로 돌아왔으면 길이 비교
            if vis:                                 # 만약 들어온 값이 있다면(없으면 0이 들어가는데, 없을 때는 -1이 출력되어야 함)
                rst = vis.split()                   # 기존에 str으로 들어간 값을 띄어쓰기 기준으로 잘라서 리스트화시킴(갯수세기위해서)
                if len(rst) > max_cnt:              # 갯수와 맥스값 비교
                    max_cnt = len(rst)              
                    continue
        if i == 4:                                  # i가 4일 경우, 방향을 다 돌았다는 뜻이므로 더 세지 않음
            continue
        if field[nx][ny].zfill(3) in vis:           # 만약 방문한 자리가 이전에 방문했던 디저트와 동일하다면 넘어감
            continue
        # 위의 예외상황을 다 넘겼다면, 같은 방향으로 한번 더 가는 경우와 방향을 꺾는 경우로 나뉘어서 다시 큐에 넣어줌
        que.append((nx,ny,i,(vis + ' ' +field[nx][ny].zfill(3))))
        que.append((nx,ny,i+1,(vis+' ' +field[nx][ny].zfill(3))))
        
dx = [1,1,-1,-1] # ↙↘↗↖
dy = [-1,1,1,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [input().split() for _ in range(N)]
    max_cnt = -1 # 발견 못할 경우 -1이니까, -1을 기본값 설정
    for i in range(N):
        for j in range(N):
            BFS(i,j,0)
    print(f'#{tc} {max_cnt}')