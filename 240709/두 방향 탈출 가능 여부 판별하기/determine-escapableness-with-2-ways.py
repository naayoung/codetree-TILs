import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
graph = []
for _ in range(n+1):
    graph.append(list(map(int, input().split())))
    
answer = [[0]* m for _ in range(n)]
visited = [[0]* m for _ in range(n)]
order = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False  
    if visited[x][y] or graph[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    global order

    dxs, dys = [1, 0], [0, 1]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            answer[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = 1

            dfs(new_x, new_y)

answer[0][0] = order
order += 1
visited[0][0] = 1

dfs(0, 0)
if answer[n-1][m-1] == 0:
    print(0)
else:
    print(1)