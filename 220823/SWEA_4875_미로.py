def dfs(x,y):
    global flag
    if flag == 1:
        return
    field[x][y] = 0
    dfs_list.append((x,y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if field[nx][ny] == 0 and (nx,ny) not in dfs_list:
                dfs(nx,ny)
            elif field[nx][ny] == 3:
                flag = 1

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    field = [list(map(int,input())) for _ in range(N)]
    dfs_list = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] == 2:
                x = i
                y = j
                break
    flag = 0
    dfs(x,y)
    print(f'#{test_case} {flag}')