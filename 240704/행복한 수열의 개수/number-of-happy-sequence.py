import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

count = 0
graph2 = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(graph[j][i])
    graph2.append(row)
    temp = set(graph[i])
    temp2 = set(graph2[i])

    if len(temp) < 3 or len(temp2) < 3:
        count += 1
print(count)