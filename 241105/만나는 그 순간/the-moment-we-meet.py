n, m = map(int, input().split())

a, b = [], []
temp_a = 0
temp_b = 0
for _ in range(n):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(t):
            temp_a += 1
            a.append(temp_a)
    else:
        for i in range(t):
            temp_a -= 1
            a.append(temp_a)
    
for _ in range(m):
    d, t = input().split()
    t = int(t)
    if d == 'R':
        for i in range(t):
            temp_b += 1
            b.append(temp_b)
    else:
        for i in range(t):
            temp_b -= 1
            b.append(temp_b)

for i in range(len(a)):
    if a[i] == b[i]:
        answer = i+1
        break
print(answer)