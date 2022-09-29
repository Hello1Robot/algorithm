# def DFS(x,y,c):
#     global min_res
#     if x == N-1 and y == N-1:
#         if min_res > c :
#             min_res = c
#     elif min_res < c:
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= N or nx < 0 or ny >= N or ny < 0:
#             continue
#         if (nx,ny) not in root:
#             if field[nx][ny] > field[x][y]:
#                 root.append((nx,ny))
#                 DFS(nx,ny,c+(field[nx][ny]-field[x][y])+1)
#                 root.pop()
#             else:
#                 root.append((nx,ny))
#                 DFS(nx,ny,c+1)
#                 root.pop()          


# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     field = [list(map(int,input().split())) for _ in range(N)]
#     res_list = []
#     root = []
#     min_res = 9999999
#     DFS(0,0,0)
#     print(f'#{tc} {min_res}')

def DFS(x,y,c,root):
    global min_res
    if x == N-1 and y == N-1:
        if min_res > c + len(root)-1:
            min_res = c + len(root)-1
    elif min_res <= c + len(root)-1:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        if (nx,ny) not in root:
            if field[nx][ny] > field[x][y]:
                root.append((nx,ny))
                DFS(nx,ny,c+(field[nx][ny]-field[x][y]),root)
                root.pop()
            else:
                root.append((nx,ny))
                DFS(nx,ny,c,root)
                root.pop()          


dx = [0,0,-1,1]
dy = [1,-1,0,0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(map(int,input().split())) for _ in range(N)]
    res_list = []
    min_res = 9999999
    DFS(0,0,0,[(0,0)])
    print(f'#{tc} {min_res}')