import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * (n+1)

def dfs(n):
    global count

    count += 1
    visited[n] = 1

    for i in graph[n]:
        if not visited[i]:
            dfs(i)

answer = []
for i in range(1, n+1):
    count = 0
    visited = [0] * (n+1)

    dfs(i)
    answer.append(count)

answer2 = []
for i in range(n):
    if answer[i] == max(answer):
        answer2.append(i+1)
print(*answer2)