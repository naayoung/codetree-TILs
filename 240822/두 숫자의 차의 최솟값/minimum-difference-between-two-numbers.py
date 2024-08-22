n = int(input())
num = list(map(int, input().split()))

answer = max(num) - min(num)
for i in range(n):
    for j in range(i):
        if num[i] - num[j] < answer:
            answer = num[i] - num[j]
print(answer)