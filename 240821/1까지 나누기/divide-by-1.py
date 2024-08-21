n = int(input())

cnt = 0
for i in range(1, n):
    if n <= 1:
        print(cnt)
        break
    else:
        n = n//i
        cnt += 1