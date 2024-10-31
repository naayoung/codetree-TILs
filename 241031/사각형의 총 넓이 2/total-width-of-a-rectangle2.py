n = int(input())
offset = 100
max_r = 200

box = [[0 for col in range(max_r+1)] for row in range(max_r+1)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            box[x][y] += 1

ans = 0
for x in range(max_r+1):
    for y in range(max_r+1):
        if box[x][y]:
            ans += 1
print(ans)