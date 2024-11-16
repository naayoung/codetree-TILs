import sys
input = sys.stdin.readline

n = int(input().strip())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for _ in range(n):
    a, b = input().split()
    b = int(b)

    if a == 'E':
        x, y = x+dx[0]*b, y+dy[0]*b
    if a == 'S':
        x, y = x+dx[1]*b, y+dy[1]*b
    if a == 'W':
        x, y = x+dx[2]*b, y+dy[2]*b
    if a == 'N':
        x, y = x+dx[3]*b, y+dy[3]*b
print(x, y)
