n = int(input())
num = list(map(int, input().split()))

for i in range(n):
    num[i] = abs(num[i])

print(*num)