a = input()
b = input()

cnt = 0
for i in range(2, len(a)+1, 2):
    if a[i-2:i] == b:
        cnt += 1
print(cnt)