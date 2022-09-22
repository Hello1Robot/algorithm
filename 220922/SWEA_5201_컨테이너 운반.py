T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    컨테이너들 = list(map(int,input().split()))
    컨테이너들.sort()
    트럭들 = list(map(int,input().split()))
    트럭들.sort()
    무게들 = 0
    while 트럭들 and 컨테이너들:
        힘쎈트럭 = 트럭들.pop()
        while 컨테이너들:
            개무거운컨테이너 = 컨테이너들.pop()
            if 힘쎈트럭 >= 개무거운컨테이너:
                무게들 += 개무거운컨테이너
                break
    print(f'#{tc} {무게들}')