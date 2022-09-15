# 중위순회 하면서 값을 채워넣기
# 노드 값 확인하기

def 중위순회(start):
    global cnt # 중위순회하면서 cnt값 넣어주기
    if start:
        중위순회(ch1[start])
        val[start] = cnt
        cnt += 1
        중위순회(ch2[start])

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # N은 노드의 갯수. N//2에 저장된 값 출력해야됨
    cnt = 1
    val = [0] * (N+1) # 노드에 값 저장할 리스트 초기화
    ch1 = [0] * (N+1) # 왼쪽자식 초기화
    ch2 = [0] * (N+1) # 오른쪽자식 초기화
    for i in range(2,N+1): # 자식 집어넣기
        if ch1[i//2]:
            ch2[i//2] = i
        else:
            ch1[i//2] = i

    중위순회(1)
    print(f'#{test_case} {val[1]} {val[N//2]}')