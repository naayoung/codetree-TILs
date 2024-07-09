import sys
input = sys.stdin.readline

n = int(input().strip())
graph = []
for _ in range(n+1):
    graph.append(list(map(int, input().split())))

answer = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
#사람 수
people = []
count = 0

#범위 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

#방문 여부 및 벽 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    global count
    
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            #방문 체크
            visited[new_x][new_y] = 1
            #존재하는 사람 추가
            count += 1
            answer[new_x][new_y] = count

            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = 1
            count = 1

            #확인용
            answer[i][j] = 1

            dfs(i, j)

            #탐색 끝난 경우 마을 사람 수 저장
            people.append(count)

#오름차순 정렬
people.sort()

print(len(people))
for i in people:
    print(i)

#print(answer)