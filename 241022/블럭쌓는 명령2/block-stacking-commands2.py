n, k = map(int, input().split())

answer = [0] * n
for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        answer[i-1] += 1
print(max(answer))