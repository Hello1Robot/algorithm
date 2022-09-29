def find_set(x): # x와 rep[x]가 같을 때까지 탐색. 집합의 대표자를 찾는 과정
    while x != rep[x]: # 대표자를 찾을 때까지 순회하기
        x = rep[x]
    return x

def union_set(x,y): # 두 집합을 합치기
    rep[find_set(x)] = find_set(y) # a그룹의 대표자를 b그룹의 대표자를 지목하게 바꾸기
    

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # 노드의 수, 간선의 수 받기
    rep = [i for i in range(V+1)] # 지목하는 대상을 등록할 리스트 만들기
    edge = [] # 간선과 가중치(비용) 담을 리스트
    for _ in range(E): # 간선 엣지에 담기
        s,e,w = map(int,input().split())
        edge.append((w,s,e)) 
        # 엣지에 비용, 시작점, 끝점 담아두기. 비용 먼저 담으면 sort를 그냥 하면 되고, 비용을 다른 순서로 담으면 lambda함수를 사용해야 함
    edge.sort()
    total = 0 # 전체 비용 계산할 토탈변수 선언
    # cnt = 0 # 왜필요한지 모르겠음. 생각해봐야할듯 
    for w,s,e in edge:
        if find_set(s) != find_set(e):
            cnt += 1
            union_set(s, e)
            total += w

            # if cnt == V:
            #     break
    print(f'#{tc} {total}')