b, a = map(int, input().split())
num = []

for i in range(a, b+1):
    if i%2 != 0:
        num.append(i)

num.sort(reverse=True)
print(*num)