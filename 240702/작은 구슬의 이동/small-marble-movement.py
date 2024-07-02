import sys
input = sys.stdin.readline

n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
dir_num = mapper[d]

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

while t > 0:
    t -= 1
    r, c = r + dxs[dir_num], c + dys[dir_num]
    if not in_range(r, c):
        dir_num = 3 - dir_num
        t += 1
print(r+1, c+1)