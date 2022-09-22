T = int(input())
for tc in range(1,T+1):
    결과 = 0
    카드뭉치 = list(map(int,input().split()))
    카드뭉치.reverse()
    A카드 = {i:0 for i in range(10)}
    B카드 = {i:0 for i in range(10)}
    flag = 1
    A카드[카드뭉치.pop()] += 1
    B카드[카드뭉치.pop()] += 1
    A카드[카드뭉치.pop()] += 1
    B카드[카드뭉치.pop()] += 1
    while 카드뭉치 and flag:
        A거 = 카드뭉치.pop()
        A카드[A거] += 1
        if A카드[A거] == 3:
            결과 = 1
            break
        for i in range(8):
            if A카드[i] > 0 and A카드[i+1] > 0 and A카드[i+2] > 0:
                결과 = 1
                flag = 0
                break
        if not flag:
            break
        B거 = 카드뭉치.pop()
        B카드[B거] += 1
        if B카드[B거] == 3:
            결과 = 2
            break
        for i in range(8):
            if B카드[i] > 0 and B카드[i+1] > 0 and B카드[i+2] > 0:
                결과 = 2
                flag = 0
                break
    print(f'#{tc} {결과}')    