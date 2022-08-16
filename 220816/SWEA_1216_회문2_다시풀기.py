import sys

sys.stdin = open("1216.txt")

input = sys.stdin.readline

for _ in range(10):
    test_case = int(input())
    field = [list(input()) for _ in range(100)]
    max_cnt = [] # 회문 길이 저장할 리스트
    for i in range(100): # x축 (y축 동일)
        for j in range(100): # 시작점
            for x in range(100): # 끝점
                st1 = ''
                st2 = ''
                for y in range(j, 100-x): # 시작점과 끝점 좁혀감
                    st1 += field[i][y] # 처음부터 시작 / 가로
                    st2 += field[y][i] # 처음부터 시작 / 세로
                   
                if st1 == st1[::-1]: # 회문이면 각각 값 추가
                    max_cnt.append(len(st1))
                if st2 == st2[::-1]:
                    max_cnt.append(len(st2))
    print(f'#{test_case} {max(max_cnt)}') # 제일 큰 값 출력