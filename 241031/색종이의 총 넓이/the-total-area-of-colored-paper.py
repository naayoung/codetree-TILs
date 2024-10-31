n = int(input())
offset = 100
max_r = 200
box = [[0 for col in range(max_r+1)] for row in range(max_r+1)]

for _ in range(n):
    x, y = map(int, input().split())
    x, y = x+offset, y+offset
    
    for i in range(x, x+8):
        for j in range(y, y+8):
            box[i][j] = 1

ans = 0
for x in range(max_r+1):
    for y in range(max_r+1):
        if box[x][y]:
            ans += 1
print(ans)