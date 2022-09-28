def dfs(start):
    stk = []
    stk.append(start)
    visited[start] = 1
    while stk:
        x = stk.pop()
        print(x, end=' ')
        for i in range(10):
            if field[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stk.append(i)


nums = list(map(int,input().split()))

field = [[0]*10 for _ in range(10)]
visited = [0]*10

for i in range(0,len(nums),2):
    start, end = nums[i], nums[i+1]
    field[start][end] = 1
    field[end][start] = 1

dfs(1)
print()
