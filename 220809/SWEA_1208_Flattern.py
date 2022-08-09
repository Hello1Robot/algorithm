import sys

sys.stdin = open('1208.txt')

T = 10

for test_case in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))
    box_list.sort()
    cnt = 1
    while cnt <= N:
        box_list[-1] -= 1
        box_list[0] += 1
        box_list.sort()
        cnt += 1
    
    print(f'#{test_case} {box_list[-1]-box_list[0]}')