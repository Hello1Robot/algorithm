# 자식부터 올라가서 부모의 값을 채워넣는 방식
# 리프노드가 홀수일 때와 짝수일 때를 나눠서 할까
# 그냥 홀수일 때에는 뒤에 하나 추가만 해주면 되나?
# 흐으으으으음
# 다이나믹프로그래밍 같은 느낌으로
# 리프노드로 조상노드까지 다 채우면서
# 만약에 목표로 하는 노드에 도달했을 경우
# 출력하고 브레이크 하는 형식으로 구현하면 될 듯
import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(1,T+1):
    N, M, L = map(int,input().split()) # N은 전체 노드, M은 리프노드의 수, L은 목표
    nodes = [0] * (N+2) # 노드값 넣을 리스트 미리 만들어놓기
    for _ in range(M):
        node, value = map(int,input().split())
        nodes[node] = value

    for i in range(N-M,0,-1):
        a = i * 2 # 자식노드 구하기
        nodes[i] = nodes[a] + nodes[a+1]
        if i == L:
            print(f'#{test_case} {nodes[L]}')     
            break      

