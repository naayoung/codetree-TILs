n = int(input())
num = list(map(int, input().split()))

answer = []

for i in range(n-1, -1, -1):
    if num[i]%2 == 0:
        answer.append(num[i])
print(*answer)