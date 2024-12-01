import sys
input = sys.stdin.readline

time = input().rstrip()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
d = 3 #북쪽

ans = -1
temp = 0
for t in time:
    temp += 1
    if t == 'L': #왼쪽 회전
        d = (d-3+2)%4
    if t == 'R': #오른쪽 회전
        d = (d+3)%4
    if t == 'F': #이동
        x, y = x+dx[d], y+dy[d]
        if x == 0 and y == 0:
            ans = temp
            break
print(ans)
