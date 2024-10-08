import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
count = 0

#범위 내 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

#가능인지 확인
def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] <= k:
        return False
    return True

def dfs(x, y, k):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if can_go(nx, ny, k):
            visited[nx][ny] = 1
            dfs(nx, ny, k)

def get_zone_num(k):
    global count, visited
    
    #초기화
    count = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = 1
                count += 1

                dfs(i, j, k)

max_zone_num = -1
answer_k = 0
max_height = 100
for k in range(1, max_height+1):
    get_zone_num(k)
    
    if count > max_zone_num:
        max_zone_num, answer_k = count, k

print(answer_k, max_zone_num)