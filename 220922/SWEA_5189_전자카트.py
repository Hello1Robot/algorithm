def f(i,k,r):                                   #  순열만드는 함수
    global min_tot                              # 최소값 비교
    if i == r:                                  # 순열 완성되면
        cnt = 0                                 # 카운트 초기화
        for x in range(1,N+1):                  # for문돌림
            cnt += field[p[x-1]][p[x]]          # 1-4-3-2-1 이라면 이 순서대로 값 비교함. 인덱스니까 -1 해줌
        if cnt < min_tot:                       # 토탈값과 최소값 비교
            min_tot = cnt                       # 최신화
    else:
        for j in range(k):
            if used[j] == 0:                    # a[j] 가 아직 사용되지 않았으면
                used[j] = 1                     # a[j] 사용됨으로 표시
                p[i] = a[j]                     # p[i]는 a[j]로 결정
                f(i+1, k,r)                     # p[i+1] 값을 결정하러 이동
                used[j] = 0                     # a[j]를 다른 자리에서 쓸 수 있도록 해제



T = int(input())
for tc in range(1,T+1):
    N = int(input())                            # 원소 갯수 받기
    field = [list(map(int,input().split())) for _ in range(N)] # 필드 선언

    a = list(range(N))                          # 인덱스값으로 쓸 숫자들.
    used = [1]+([0] * (N-1))                    # 첫번째는 0번째 인덱스로 고정이니까, 항상 방문했다고 선언해둠
    p = [0] * (N+1)                             # 맨 뒤에도 처음 있던 곳으로 돌아와야 하기 때문에 N+1개를 만듦
    min_tot = 100000000                         # 최소값카운트에 대충 적당히 큰 값 넣기
    f(1, N, N)                                  # 0번째 칸은 고정. 1번째 칸부터 돌리면 됨
    print(f'#{tc} {min_tot}')