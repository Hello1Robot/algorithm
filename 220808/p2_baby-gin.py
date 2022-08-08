# 문제풀이 아이디어 먼저 작성 (17:08분 ~ 17:18분)
# 카드 6장을 0~9인 리스트에 넣어둠
# 먼저, 같은 카드가 3장인 경우를 확인함
# 있으면 남은 카드가 연속되는지 확인
# 없다면 연속된 두 쌍의 카드가 존재하는지 확인
T = int(input())
for test_case in range(1, T+1):
    nums = list(map(int, input()))
    num_list = [0]*10
    cnt = 0
    for i in nums:
        num_list[i] += 1

    for j in range(len(num_list)):
        if num_list[j] >= 6:
            num_list[j] -= 6
            cnt += 2
        elif num_list[j] >= 3:
            num_list[j] -= 3
            cnt += 1


    for x in range(len(num_list)-2):
        if num_list[x] != 0 and num_list[x+1] != 0 and num_list[x+2] != 0:
            num_list[x] -= 1
            num_list[x+1] -= 1
            num_list[x+2] -= 1
            cnt += 1
        if num_list[x] != 0 and num_list[x+1] != 0 and num_list[x+2] != 0:
            num_list[x] -= 1
            num_list[x+1] -= 1
            num_list[x+2] -= 1
            cnt += 1


    if cnt == 2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')