import sys

sys.stdin = open("1216.txt")

input = sys.stdin.readline

for _ in range(10):
    test_case = int(input())
    field = [list(input()) for _ in range(100)]
    max_cnt = 0
    for i in range(100): #x,y축

        for j in range(100): #0부터 99까지

            for z in range(100):
                st1 = ''
                st2 = ''
                st3 = ''
                st4 = ''
                for x in range(z,100-j): # j값 뺀만큼 셀 수 있음
                    st1 += field[i][j+x]
                    st2 += field[j+x][i]
                    st3 += field[i][99-x-j]
                    st4 += field[99-x-j][i]
                if st1 == st1[::-1]:
                    if len(st1) > max_cnt:
                        max_cnt = len(st1)
                if st2 == st2[::-1]:
                    if len(st2) > max_cnt:
                        max_cnt = len(st2)
                if st3 == st3[::-1]:
                    if len(st3) > max_cnt:
                        max_cnt = len(st3)
                if st4 == st4[::-1]:
                    if len(st4) > max_cnt:
                        max_cnt = len(st4)



    
    print(max_cnt)
    