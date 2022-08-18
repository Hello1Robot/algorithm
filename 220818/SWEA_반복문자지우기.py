T = int(input())

for test_case in range(1,T+1):
    st = list(input())
    cnt = True
    while cnt:

        for i in range(len(st)-1):
            if st[i] == st[i+1]:
                st.pop(i+1)
                st.pop(i)
                break
        else:
            cnt = False
    print(f'#{test_case} {len(st)}')
