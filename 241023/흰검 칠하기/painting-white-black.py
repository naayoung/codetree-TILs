n = int(input())

temp1 = [0]*200001
temp2 = [0]*200001
color = ['']*200001
m = 100000
for _ in range(n):
    a, b = input().split()
    a = int(a)

    if b == 'L':
        for i in range(m-a+1, m+1):
            temp1[i] += 1
            if temp1[i] >= 2 and temp2[i] >= 2:
                color[i] = 'G'
            if color[i] != 'G':
                color[i] = 'W'
        m = m-a+1
    else:
        for i in range(m, m+a):
            temp2[i] += 1
            if temp1[i] >= 2 and temp2[i] >= 2:
                color[i] = 'G'
            if color[i] != 'G':
                color[i] = 'B'
        m = m+a-1

c1, c2, c3 = 0, 0, 0
for i in color:
    if i == 'W':
        c1 += 1
    if i == 'B':
        c2 += 1
    if i == 'G':
        c3 += 1
print(c1, c2, c3)