n, m = map(int, input().split())

a, b = {}, {}
time_a, time_b = 0, 0
distance_a, distance_b = 0, 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        time_a += 1
        distance_a += v
        a[time_a] = distance_a

for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        time_b += 1
        distance_b += v
        b[time_b] = distance_b   

answer = 0
m = ''
max_time = max(time_a, time_b)
for i in range(1, max_time+1):
    if m == '':
        if a[i] < b[i]:
            m = 'B' 
        elif a[i] > b[i]:
            m = 'A'
    elif m == 'A' and a[i] < b[i]:
        answer += 1
        m = 'B'
    elif m == 'B'and a[i] > b[i]:
        answer += 1
        m = 'A'
print(answer)