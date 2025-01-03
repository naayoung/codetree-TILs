x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Write your code here!
OFFSET = 1000
MAX_R = 2000

n = 2
checked = [[0]*(MAX_R+1) for _ in range(MAX_R+1)]

for i in range(n):
    # OFFSET을 더해줌
    start_x, start_y, end_x, end_y = x1[i] + OFFSET, y1[i] + OFFSET, x2[i] + OFFSET, y2[i] + OFFSET
    
    # 직사각형 영역에 번호 부여
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            checked[x][y] = i + 1

min_x, min_y, max_x, max_y = MAX_R, MAX_R, 0, 0
check_exist = False
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] == 1:
            check_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if check_exist:
    area = (max_x - min_x+1) * (max_y - min_y+1)
else:
    area = 0
print(area)
