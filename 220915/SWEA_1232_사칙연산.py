# 오늘 풀었던 노드의합과 흡사한 문제
# 리프노드에 값이 들어가고 나머지 노드에 연산자가 들어감


def 후위순회(start):
    if start:
        if nodes[start] in 연산자:
            a = 후위순회(left[start])
            b = 후위순회(right[start])
            if nodes[start] == '+':
                return a + b
            elif nodes[start] == '-':
                return a - b
            elif nodes[start] == '*':
                return a * b
            elif nodes[start] == '/':
                return a // b
        else:
            return nodes[start] 


for test_case in range(1,11):
    N = int(input())
    nodes = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    연산자 = ['+','-','*','/']
    for _ in range(N):
        node, val, *sons = input().split()
        node = int(node)
        if val in 연산자:
            nodes[node] = val
            for son in sons:
                if left[node]:
                    right[node] = int(son)
                else:
                    left[node] = int(son)
        else:
            nodes[node] = int(val)

    print(f'#{test_case} {후위순회(1)}')

    