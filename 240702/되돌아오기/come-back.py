import sys
input = sys.stdin.readline

#입력값
n = int(input().strip())

#방향
mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
dx, dy = 0, 0
count = 0
answer = -1
for _ in range(n):
    dir_num, m = map(str, input().split())
    m = int(m)

    for _ in range(m):
        dx, dy = dx + dxs[mapper[dir_num]], dy + dys[mapper[dir_num]]
        count += 1
        if dx == x and dy == y:
            answer = count
            break
print(answer)