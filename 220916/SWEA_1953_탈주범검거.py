#  솔루션 코드를 작성합니다.
# 다양한 터널 구조물모양 고려하기
# 튜플로 좌표 다 넣기
# 튜플 길이 세기
# 왔던 길로 다시 가기 가능
# 레벨에 도달하면 종료
from collections import deque


def 너비우선탐색(x, y):
    cnt = 0
    que = deque()
    visited[x][y] = 1
    que.append((x, y))
    while que:
        x, y = que.popleft()
        pipe_type = field[x][y]
        for dx, dy in pipe_delta[pipe_type]:
            nx = x + dx
            ny = y + dy
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            if (dx, dy) == (-1, 0):  # 방향이 위쪽이면
                if field[nx][ny] in [1, 2, 5, 6] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
            elif (dx, dy) == (1, 0):  # 방향이 아래쪽이면
                if field[nx][ny] in [1, 2, 4, 7] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
            elif (dx, dy) == (0, -1):  # 방향이 왼쪽이면
                if field[nx][ny] in [1, 3, 4, 5] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
            elif (dx, dy) == (0, 1):  # 방향이 오른쪽이면
                if field[nx][ny] in [1, 3, 6, 7] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= level:
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M, start_x, start_y, level = map(int, input().split())  # x축 y축 맨홀x,y축 도달레벨
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    # 상하좌우
    pipe_delta = [[], [(1, 0), (-1, 0), (0, -1), (0, 1)], [(1, 0), (-1, 0), (0, 0), (0, 0)],
                  [(0, 0), (0, 0), (0, 1), (0, -1)], [(0, 0), (-1, 0), (0, 0), (0, 1)],
                  [(1, 0), (0, 0), (0, 1), (0, 0)], [(0, 0), (0, -1), (0, 0), (1, 0)],
                  [(0, 0), (-1, 0), (0, -1), (0, 0)]]
    print(f'#{test_case} {너비우선탐색(start_x, start_y)}')