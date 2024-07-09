import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
count = -1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visited[v] = True

    global count
    count += 1
    
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

dfs(1)
print(count)