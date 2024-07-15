import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_length = 0
for i in graph:
    if len(i) > max_length:
        max_length = len(i)

answer = 0
for i in range(len(graph)):
    if max_length == len(graph[i]):
        answer = i
print(*graph[answer])