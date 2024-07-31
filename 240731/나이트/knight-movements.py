import sys
from collections import deque
input = sys.stdin.readline

# 변수 선언 및 입력
n = int(input().strip())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

# bfs에 필요한 변수들
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque()

count = sys.maxsize

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1:
        return False
    return True

def bfs():
    global count
    while q:
        x, y = q.popleft()

        dxs = [-2, -2, -1, -1,  1, 1,  2, 2]
        dys = [-1,  1, -2,  2, -2, 2, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

        # 도착지에 가는 것이 가능할때만
        # 답을 갱신해줍니다.
        if visited[r2][c2]:
            count = graph[r2][c2]

visited[r1][c1] = 1
graph[r1][c1] = 0
q.append((r1, c1))
bfs()


# 출력:
if count == sys.maxsize:  # 불가능한 경우라면
    count = -1        # -1을 답으로 넣어줍니다.

print(count)