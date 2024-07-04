import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

if n > 1 and m == 1:
    print(n*(n-1))
elif n == 1:
    print(2)
else:
    count = 0
    graph2 = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(graph[j][i])
        graph2.append(row)
        temp = set(graph[i])
        temp2 = set(graph2[i])

        if len(temp) < m+1 or len(temp2) < m+1:
            count += 1
    print(count)