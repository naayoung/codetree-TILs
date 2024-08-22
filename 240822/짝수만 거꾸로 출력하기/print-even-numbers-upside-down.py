n = int(input())
num = list(map(int, input().split()))

answer = []

for i in range(n, -1, -1):
    if i%2 == 0:
        answer.append(i)
print(*answer)