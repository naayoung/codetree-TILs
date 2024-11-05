n, m, k = map(int, input().split())

stu = [0]*(n+1)
answer = -1
for _ in range(m):
    t = int(input())
    stu[t] += 1

    if stu[t] >= k:
        answer = t
        break
print(answer)