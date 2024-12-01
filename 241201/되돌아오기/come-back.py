import sys
input = sys.stdin.readline

dir = {
    'W':2,
    'S':1,
    'N':3,
    'E':0
}

n = int(input().strip())

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

ans = -1
time = 0
for _ in range(n):
    dr, dd = input().split()
    dr, dd = dir[dr], int(dd)

    for _ in range(dd):
        x, y = x+dx[dr], y+dy[dr]

        time += 1
        if x == 0 and y == 0:
            ans = time
            break
        break

print(ans)

