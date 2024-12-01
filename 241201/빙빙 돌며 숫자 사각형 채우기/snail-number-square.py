import sys
input = sys.stdin.readline

#n행 m열
n, m = map(int, input().split())
temp = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
d = 0

temp[x][y] = 1

for i in range(2, n*m+1):
    nx, ny = x+dx[d], y+dy[d]

    if not in_range(nx, ny) or temp[nx][ny] != 0:
        d = (d+1)%4
    
    x, y = x+dx[d], y+dy[d]
    temp[x][y] = i

for t in temp:
    print(*t)