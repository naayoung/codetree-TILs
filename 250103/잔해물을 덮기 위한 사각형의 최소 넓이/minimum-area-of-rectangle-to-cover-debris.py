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
    for x in range(start_x, end_x):  # x1부터 x2까지
        for y in range(start_y, end_y):  # y1부터 y2까지
            checked[x][y] = i + 1  # 번호는 1부터 시작

min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# 넓이 계산
if not first_rect_exist:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)