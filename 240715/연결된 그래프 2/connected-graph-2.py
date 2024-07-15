import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [0] * (n+1)
count = 0
answer = []

def dfs(v):
    global count
    visited[v] = 1
    count += 1

    for nv in graph[v]:
        if not visited[nv]:
            visited[nv] = 1
            dfs(nv)

for i in range(1, n+1):
    count = 0
    visited = [0] * (n+1)

    dfs(i)
    answer.append((i, count))

# 갈 수 있는 최대 노드 수를 구합니다.
maxNode = max(answer, key=lambda x: x[1])[1]

# 갈 수 있는 최대 노드 수에 해당하는 노드 번호를 출력합니다.
for node, count in answer:
    if count == maxNode:
        print(node, end=" ")