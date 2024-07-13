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

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global count

    count += 1
    visited[x][y] = 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            dfs(nx, ny)

answer = []
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            count = 0
            visited[i][j] = 1

            dfs(i, j)
            answer.append(count)
print(len(answer))
for i in answer:
    print(i)