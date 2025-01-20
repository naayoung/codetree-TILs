n, m = map(int, input().split())

# Write your code here!
graph = [[0]*m for _ in range(n)]

x, y = 0, 0
dir_num = 1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

graph[x][y] = 1
for i in range(2, n*m+1):
    dx, dy = x+dxs[dir_num], y+dys[dir_num]

    if not in_range(dx, dy) or graph[dx][dy] != 0:
        dir_num = (dir_num-1+4)%4

    x, y = x+dxs[dir_num], y+dys[dir_num]
    graph[x][y] = i

for g in graph:
    print(*g)