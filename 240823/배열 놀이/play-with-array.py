n, q = map(int, input().split())
num = list(map(int, input().split()))
qum = [list(map(int, input().split())) for _ in range(q)]

for qu in qum:
    if qu[0] == 1:
        print(num[qu[1]-1])
    if qu[0] == 2:
        if qu[1] in num:
            print(num.index(qu[1])+1)
        else:
            print(0)
    if qu[0] == 3:
        print(*(num[qu[1]-1:qu[2]]))