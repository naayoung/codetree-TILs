m = input()

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3

for mm in m:
    if mm =='L':
        dir_num = (dir_num-1+4)%4
    if mm =='R':
        dir_num = (dir_num+1)%4
    if mm =='F':
        x, y = x+dx[dir_num], y+dy[dir_num]

print(x, y)