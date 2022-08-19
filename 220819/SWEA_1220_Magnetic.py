# 마그네틱 아이디어 정리
# x열을 기준으로 검사한다.
# 1은 위로, 2는 아래로 간다.
# 위에서 아래로 검사하므로, 스택이 비었을 때 1이 들어오면, 날린다.
# 2가 들어오면 킵.
# 2가 들어갈 때, 이전에 있던 게 2면 넣지않는다.
# 2가 맨 위일 때, 1이 들어가면 둘 다 날리고 카운트를 1 추가한다.
# 줄마다 나뉘어서 반복한다.

for test_case in range(1, 11):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        stack = []
        for i in range(N):
            if field[i][j] == 2:
                if stack:
                    stack.pop()
                    cnt += 1
            if field[i][j] == 1:
                if not stack:
                    stack.append(field[i][j])
    print(f'#{test_case} {cnt}')