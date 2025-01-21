n = int(input())
grid = [[0] * n for _ in range(n)]

# Write your code here!
#끝에서 시작
x, y = n-1, n-1
dir_num = 2
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

grid[x][y] = n*n

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(n*n-1, 0, -1):
    dx, dy = x+dxs[dir_num], y+dys[dir_num]
    if not in_range(dx, dy) or grid[dx][dy] != 0:
        dir_num = (dir_num+1)%4
    
    x, y = x+dxs[dir_num], y+dys[dir_num]
    grid[x][y] = i

for g in grid:
    print(*g)