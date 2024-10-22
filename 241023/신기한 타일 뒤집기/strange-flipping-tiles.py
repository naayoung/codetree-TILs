n = int(input())

color = ['']*200001
m = 100000
for _ in range(n):
    a, b = input().split()
    a = int(a)

    if b == 'L':
        for i in range(m-a, m):
            color[i] = 'W'
        m = m-a
    else:
        for i in range(m, m+a):
            color[i] = 'B'
        m = m+a
ans = [0, 0]
for i in color:
    if i == 'W':
        ans[0] += 1
    if i == 'B':
        ans[1] += 1
print(*ans)