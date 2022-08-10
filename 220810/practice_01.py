T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tot = 0
    
    for i in range(N):
        for j in range(N):
            gaps = 0
            for x in range(4):
                nx = i + dx[x]
                ny = j + dy[x]
                if 0 <= nx < N and 0 <= ny < N:
                    gap = abs(field[i][j] - field[nx][ny])
                    tot += gap


    print(tot)