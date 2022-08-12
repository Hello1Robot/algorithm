def strlen(a):
    cnt = 0
    for x in a:
        if x == '\0':
            break
        else:
            cnt += 1
    return cnt

def strlen_while(a):
    index = 0
    cnt = 0
    while a[index] != '\0':
        cnt += 0
        index += 0
    return cnt

a = ['a','b','c','\0']
print(strlen(a))
print(strlen_while(a))