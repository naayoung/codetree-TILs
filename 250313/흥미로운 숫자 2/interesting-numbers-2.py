X, Y = map(int, input().split())

# Please write your code here.
cnt = 0
for w in range(X, Y+1):
    w = str(w)
    temp = [0]*10
    for i in w:
        i = int(i)
        temp[i] += 1
        
    t, tt = 0, 0
    for i in temp:
        if i == 0:
            t += 1
        elif i == 1:
            tt += 1
    if t == 8 and tt == 1:
        cnt += 1

print(cnt)