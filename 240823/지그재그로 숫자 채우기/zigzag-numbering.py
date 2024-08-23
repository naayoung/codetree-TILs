n, m = map(int, input().split())
answer = [[0]*m for _ in range(n)]

num = 0
for mm in range(m):
    if mm%2 == 0:
        for i in range(n):
            answer[i][mm] = num
            num += 1
    else:
        for i in range(n-1, -1, -1):
            answer[i][mm] = num
            num += 1

for ans in answer:
    print(*ans)