# 트리 구조를 만들고
# 서브 트리를 순회하도록
def search_tree(start):
    global cnt
    if start:
        cnt += 1
        search_tree(ch1[start])
        search_tree(ch2[start])

T = int(input())
for test_case in range(1,T+1):
    N, start = map(int,input().split())
    nodes = list(map(int,input().split()))
    cnt = 0
    ch1 = [0] * (N+2)
    ch2 = [0] * (N+2)
    for i in range(0, 2*N, 2):
        if ch1[nodes[i]]:
            ch2[nodes[i]] = nodes[i+1]
        else:
            ch1[nodes[i]] = nodes[i+1]
    search_tree(start)
    print(f'#{test_case} {cnt}')
