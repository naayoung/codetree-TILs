import sys
input = sys.stdin.readline

r = input().strip()
n = len(r)

x, y = 0, 0
dir_num = 3

time = 0
answer = -1
for i in range(n):

    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    time += 1
    
    if r[i] == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    if r[i] == 'R':
        dir_num = (dir_num + 1) % 4
    if r[i] == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]

    if x == 0 and y == 0:
        answer = time
        break
print(answer)