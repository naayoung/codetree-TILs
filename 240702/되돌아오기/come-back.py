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
count = 0
answer = -1
while n > 0:
    dir_num, m = map(str, input().split())
    m = int(m)
    n -= 1

    for _ in range(m):
        x, y = x + dxs[mapper[dir_num]], y + dys[mapper[dir_num]]
        count += 1

        if x == 0 and y == 0:
            answer = count
            n = 0
print(answer)