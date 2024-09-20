def sol1(i):
    if i%2 == 0:
        return True
    return False

def sol2(i):
    temp = list(str(i))
    if temp[len(temp)-1] == '5':
        return True
    return False

def sol3(i):
    if i%3 == 0 and i%9 != 0:
        return True
    return False

a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    if sol1(i) or sol2(i) or sol3(i):
        cnt += 1
print((b-a+1)-cnt)