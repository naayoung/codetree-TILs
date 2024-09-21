n = int(input())
num = list(map(int, input().split()))

for i in range(n):
    if num[i]%2 == 0:
        num[i] = num[i]//2
print(*num)