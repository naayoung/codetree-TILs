a, b = map(int, input().split())
num = []

for i in range(a, b+1, 2):
    num.append(i)
num.sort()
print(*num)