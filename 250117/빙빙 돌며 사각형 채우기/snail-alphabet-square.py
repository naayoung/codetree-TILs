n, m = map(int, input().split())

# Write your code here!
#1. 범위 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

#2. 주어진 수에 맞는 맵 크기 그리기
graph = list([""]*m for _ in range(n))

#3. 초기값 설정
x, y = 0, 0
dir_num = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
graph[x][y] = chr(65)

#알파벳 입력
for i in range(1, n*m):
    dx, dy = x+dxs[dir_num], y+dys[dir_num]

    if not in_range(dx, dy) or graph[dx][dy] != "":
        dir_num = (dir_num+1)%4
        
    x, y = x+dxs[dir_num], y+dys[dir_num]
    graph[x][y] = chr(i+65)

#출력
for g in graph:
    print(*g)
