a, b = map(int, input().split())

temp = [i for i in range(a, b+1)]
for i in range(a, b+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt > 1:
        temp.remove(i)
if a == 1:
    print(0)
else:
    print(sum(temp))