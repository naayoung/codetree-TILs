import sys
input = sys.stdin.readline

n = int(input().strip())
num = []
for _ in range(n):
    temp = list(map(int, input().split()))
    num.append(temp)
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

answer = 0
for i in range(n):
    for j in range(n):
        count = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and num[nx][ny] == 1:
                count += 1
        if count >= 3:
            answer += 1
print(answer)