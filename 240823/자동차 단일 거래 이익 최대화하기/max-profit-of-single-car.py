n = int(input())
num = list(map(int, input().split()))

temp = [0] * n

for i in range(n-1):
    temp[i] = max(num[i:]) - num[i]
print(max(temp))