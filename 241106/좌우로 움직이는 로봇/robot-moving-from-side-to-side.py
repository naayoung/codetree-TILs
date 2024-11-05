n, m = map(int, input().split())

a, b = {}, {}
time_a, time_b = 0, 0
distance_a, distance_b = 0, 0
#a가 움직인 횟수
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for i in range(t):
        time_a += 1
        if d == 'L':
            distance_a -= 1
        if d == 'R':
            distance_a += 1
        a[time_a] = distance_a
#b가 움직인 횟수
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for i in range(t):
        time_b += 1
        if d == 'L':
            distance_b -= 1
        if d == 'R':
            distance_b += 1
        b[time_b] = distance_b

min_time = min(time_a, time_b)
answer = 1
for i in range(1, min_time+1):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        answer += 1
print(answer)