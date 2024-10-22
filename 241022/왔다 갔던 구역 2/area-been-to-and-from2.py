n = int(input())

answer = [0] * 20
m = 10
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'L':
        for i in range(m-a, m):
            answer[i] += 1
        m = m-a
    else:
        for i in range(m, m+a):
            answer[i] += 1
        m = m+a
ans = 0
for i in answer:
    if i > 1:
        ans += 1
print(ans)