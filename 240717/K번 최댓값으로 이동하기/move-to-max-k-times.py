import sys
from collections import deque

NOT_EXISTS = (-1, -1)

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
r, c = map(int, input().split())
#현재 위치
answer = (r-1, c-1)

visited = [[0] * n for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
def can_go(x, y, target_num): 
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] >= target_num:
        return False
    return True

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    x, y = answer
    visited[x][y] = 1
    q.append(answer)

    target_num = graph[x][y]

    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, target_num):
                q.append((nx, ny))
                visited[nx][ny] = 1

def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    nx, ny = new_pos
    
    return (graph[nx][ny], -nx, -ny) > (graph[best_x][best_y], -best_x, -best_y)

def move():
    global answer, visited

    visited = [[0] * n for _ in range(n)]

    bfs()
    
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j) == answer:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    
    if best_pos == NOT_EXISTS:
        return False
    else:
        answer = best_pos
        return True

for _ in range(k):
    if not move():
        break

fx, fy = answer
print(fx + 1, fy + 1)