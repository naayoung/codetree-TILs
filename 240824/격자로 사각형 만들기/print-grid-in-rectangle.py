n = int(input())

answer = [[1]*n for _ in range(n)]
for i in range(1, n):
    for j in range(1, n):
        answer[i][j] = answer[i-1][j-1] + answer[i-1][j] + answer[i][j-1]

for ans in answer:
    print(*ans)