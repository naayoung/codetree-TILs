import sys
input = sys.stdin.readline

n = int(input().strip())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def count_num(x, y):
    cnt = 0
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if num[nx][ny] == 1:
                cnt += 1
    return cnt

answer = 0
for x in range(n):
    for y in range(n):
        if count_num(x, y) >= 3:
            answer += 1
print(answer)