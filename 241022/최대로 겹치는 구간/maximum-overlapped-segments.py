n = int(input())

answer = [0] * 201
for _ in range(n):
    x1, x2 = map(int, input().split())
    x1, x2 = x1+100, x2+100
    for i in range(x1, x2):
        answer[i] += 1
print(max(answer))