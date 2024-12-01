import sys
input = sys.stdin.readline

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

def direction(d):
    if d == 'U':
        dn = 3
    if d == 'D':
        dn = 1
    if d == 'R':
        dn = 0
    if d == 'L':
        dn = 2
    return dn

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y, dn = r-1, c-1, direction(d)
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(t):
    nx, ny = r+dxs[dn], c+dys[dn]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        dn = abs(dn)
print(x+1, y+1)