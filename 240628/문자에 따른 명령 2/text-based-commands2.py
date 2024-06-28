import sys
input = sys.stdin.readline

x, y = 0, 0
dir_num = 3 #북쪽
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

arr = input().strip()
for i in arr:
    if i == "L": #반시계 방향
        dir_num = (dir_num - 1 + 4) % 4
    elif i == "R": #시계 방향
        dir_num = (dir_num + 1) % 4
    elif i == "F":
        nx, ny = x + dx[dir_num], y + dy[dir_num]
print(nx, ny)