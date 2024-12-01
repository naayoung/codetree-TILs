import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temp = [[0]*n for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check_statue(x, y):
    cnt = 0

    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if in_range(nx,ny) and temp[nx][ny] == 1:
            cnt += 1
    return cnt

for _ in range(m):
    r,c = map(int, input().split())
    r, c = r-1, c-1
    temp[r][c] = 1

    if check_statue(r,c) == 3:
        print(1)
    else:
        print(0)
