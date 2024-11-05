n, m = map(int, input().split())

a, b = [0]*1001, [0]*1001
time_a, time_b = 0, 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        time_a += 1
        a[time_a] = v*t

for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        time_b += 1
        b[time_b] = v*t   

answer = 0
m = ''
for i in range(1001):
    if m == '':
        if a[i] < b[i]:
            m = 'B' 
        else:
            m = 'A'
    elif m == 'A':
        if a[i] < b[i]:
            answer += 1
            m = 'B'
    else:
        if a[i] > b[i]:
            answer += 1
            m = 'A'
print(answer-1)