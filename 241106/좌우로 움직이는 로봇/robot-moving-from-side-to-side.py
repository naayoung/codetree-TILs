n, m = map(int, input().split())

a, b = [], []
distance_a, distance_b = 0, 0
#a가 움직인 횟수
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for i in range(t):
        if d == 'L':
            distance_a -= 1
        if d == 'R':
            distance_a += 1
        a.append(distance_a)
#b가 움직인 횟수
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for i in range(t):
        if d == 'L':
            distance_b -= 1
        if d == 'R':
            distance_b += 1
        b.append(distance_b)

# 두 리스트 중 짧은 것을 기준으로 자르고 나머지는 마지막 위치로 고정
max_time = max(len(a), len(b))
while len(a) < max_time:
    a.append(a[-1])
while len(b) < max_time:
    b.append(b[-1])

# 로봇들이 같은 위치에 오게 되는 순간을 찾기 위한 로직
answer = 0
for i in range(1, max_time):
    if a[i] == b[i] and a[i - 1] != b[i - 1]:
        answer += 1
print(answer)