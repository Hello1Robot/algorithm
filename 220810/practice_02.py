T = int(input())


for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    cnt = 0
    for i in range(1, 1<<N):
        sums = 0
        for j in range(N):
            

            if i & (1<<j):
                sums += arr[j]
            
        if  sums == 0:
            cnt += 1

    if cnt:
        print(1)
    else:
        print(0)