n, m = map(int, input().split())
num1 = [list(map(int, input().split())) for _ in range(n)]
num2 = [list(map(int, input().split())) for _ in range(n)]

answer = [[1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if num1[i][j] == num2[i][j]:
            answer[i][j] = 0
for ans in answer:
    print(*ans)