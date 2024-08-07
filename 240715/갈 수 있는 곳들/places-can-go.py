import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * n for _ in range(n)]
q = deque()
count = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 1:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1    

for _ in range(k):
    r, c = map(int, input().split())
    q.append((r-1, c-1))
    visited[r-1][c-1] = 1

bfs()

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            count += 1
print(count)