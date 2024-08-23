n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(m)]

answer = [[0]*n for _ in range(n)]
for num in nums:
    a, b = num[0], num[1]
    answer[a-1][b-1] = a*b
for ans in answer:
    print(*ans)