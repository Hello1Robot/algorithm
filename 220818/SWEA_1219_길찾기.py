def dfs(start):
    dfs_list.append(start) # 시작값 리스트에 넣기
    for y in range(len(graph[start])): # 이어진 길 탐색
        if graph[start][y] == 1 and (y not in dfs_list): # 값이 1이고 탐색한 적 없는 길이라면
            dfs(y) # 재귀로 탐색
T = 10
for test_case in range(1, T+1):

    N, M = map(int, input().split())

    graph = [[0] * (100) for _ in range(100)] # 100*100 리스트 생성
    dfs_list = [] # 탐색한 길 담을 리스트
    rst = list(map(int, input().split())) # 좌표값 받아오기
    for i in range(0,len(rst),2): # 좌표값 입력하기
        a, b = rst[i], rst[i+1]
        graph[a][b] = 1

    stt, point = 0, 99 # 시작값과 도착값 입력
    res = 0
    dfs(stt)
    if point in dfs_list: # 도착값이 있으면(도착한다면) 1
        res = 1
    print(f'#{test_case} {res}')