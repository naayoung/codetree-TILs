import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input().strip())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] != k:
        return False
    return True

def dfs(x, y, k):
    global count
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    visited[x][y] = 1
    count += 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny, k):
            dfs(nx, ny, k)

def get_block(k):
    global count, block, visited

    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if can_go(i, j, k):
                visited[i][j] = 1
                count = 0
                
                dfs(i, j, k)

                if count >= 4:
                    block += 1
                answer.append(count)


answer = []
block = 0
for k in range(1, 101):
    get_block(k)

print(block, max(answer))