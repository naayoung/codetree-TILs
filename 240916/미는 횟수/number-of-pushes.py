a = input()
b = input()

cnt = 0
while True:
    if a == b:
        print(cnt)
        break
    elif cnt > len(a):
        print(-1)
        break
    else:
        cnt += 1
        a = a[1:] + a[0]