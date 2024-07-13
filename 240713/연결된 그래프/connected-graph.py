import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)
count = 0

def dfs(n):
    global count

    for i in graph[n]:
        if not visited[i]:
            visited[i] = 1
            count += 1
            dfs(i)

visited[1] = 1
dfs(1)

print(count)