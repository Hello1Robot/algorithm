from collections import deque

def BFS(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        start = que.popleft()
        print(start, end=' ')
        for node in nodes[start]:
            if visited[node] == 0:
                visited[node] = 1
                que.append(node)


간선들 = list(map(int,input().split()))
nodes = {i:[] for i in range(1,10)}
visited = [0] * 11
for i in range(0,len(간선들),2):
    nodes[간선들[i]].append(간선들[i+1])
    nodes[간선들[i+1]].append(간선들[i])
BFS(1)
print()