import sys
input = sys.stdin.readline

#입력값
n, m = map(int, input().split())

#답안
answer = [
    [0] * n
    for _ in range(m)
]

#범위 내 확인
def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

#그래프
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0 #오른쪽(0), 아래(1), 왼쪽(2), 위(3)

#초기값 설정
x, y = 0, 0
answer[x][y] = 1
count = 1

for _ in range(2, n*m+1):
    dx, dy = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(dx, dy) or answer[dx][dy] != 0:
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    count += 1
    answer[x][y] = count

#출력
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()