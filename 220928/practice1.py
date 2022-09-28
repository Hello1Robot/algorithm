def DFS(start):
    visited[start] = 1
    print(start, end=' ')
    for node in nodes[start]:
        if visited[node] == 0:
            DFS(node)

간선들 = list(map(int,input().split()))
nodes = {i:[] for i in range(1,10)}
visited = [0] * 11
for i in range(0,len(간선들),2):
    nodes[간선들[i]].append(간선들[i+1])
    nodes[간선들[i+1]].append(간선들[i])
DFS(1)
print()
