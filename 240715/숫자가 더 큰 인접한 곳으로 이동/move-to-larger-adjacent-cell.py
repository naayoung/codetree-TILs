n, r, c = map(int, input().split())
graph = [[0] * (n+1)]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

visited_nums = []

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def can_go(x, y, curr_num):
    if not in_range(x, y):
        return False
    if graph[x][y] <= curr_num:
        return False
    return True

def simulate():
    global r, c
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy

        if can_go(nx, ny, graph[r][c]):
            r, c = nx, ny
            return True

    return False

visited_nums.append(graph[r][c])
while True:
    greater_number_exist = simulate()

    if not greater_number_exist:
        break
    
    visited_nums.append(graph[r][c])

print(*visited_nums)