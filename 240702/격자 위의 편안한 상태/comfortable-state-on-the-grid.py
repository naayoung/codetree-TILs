import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [
    [0]*n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    board[r][c] = 1

    #확인
    count = 0
    for i in range(4):
        dx, dy = r + dxs[i], c + dys[i]
        if in_range(dx, dy) and board[dx][dy] == 1:
                count += 1
    
    if count == 3:
        print(1)
    else:
        print(0)