# 방법1. 슬라이싱 날먹
a = 'algorithm'
print(a[::-1])

# 방법2. for문 돌리기
def flip(a):
    a_list = list(a)
    N = len(a_list)
    for i in range(N//2):
        a_list[i], a_list[N-1-i] = a_list[N-1-i], a_list[i]

    return ''.join(a_list)
 
print(flip(a))

# 방법3. 리버스 쓰기
list_a = list(a)
list_a.reverse()
new_a = ''.join(list_a)
print(new_a)

# 방법 4. 더하기 연산
reverse_a = ''

for idx in range(len(a)-1, -1, -1):
    reverse_a += a[idx]
print(reverse_a)