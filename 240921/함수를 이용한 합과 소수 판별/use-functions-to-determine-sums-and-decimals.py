a, b = map(int, input().split())

def sol(i):
    cnt = 0
    for x in range(2, i):
        if i%x == 0:
            cnt += 1
    if cnt == 0 and (i//10+i%10)%2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if sol(i):
        cnt += 1
print(cnt)