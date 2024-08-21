num = [int(input()) for _ in range(5)]

cnt = 0
for i in num:
    if i%2 == 0:
        cnt += 1

print(cnt)