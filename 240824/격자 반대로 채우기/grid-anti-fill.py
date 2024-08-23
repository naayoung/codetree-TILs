n = int(input())

answer = [[0]*n for _ in range(n)]

num = 1
for i in range(n-1, -1, -1):
    if (n-1-i) % 2 == 0:
        for j in range(n-1, -1, -1):
            answer[j][i] = num
            num += 1
    else:
        for j in range(n):
            answer[j][i] = num
            num += 1

for ans in answer:
    print(*ans)