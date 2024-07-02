import sys
input = sys.stdin.readline

n = int(input().strip())

info = []
for _ in range(n):
    info.append(input().strip())
k = int(input().strip())

#초기 위치
def init(num):
    if num <= n:
        return 0, num - 1, 0
    elif num <= 2 * n:
        return num - n - 1, n - 1, 1
    elif num <= 3 * n:
        return n - 1, n - (num - 2 * n), 2
    else:
        return n - (num - 3 * n), 0, 3

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir

def simulate(x, y, dir_num):
    count = 0
    while in_range(x, y):
        if info[x][y] == "/": # 0 <-> 1 / 2 <-> 3
            x, y, dir_num = move(x, y, dir_num ^ 1) #XOR
        elif info[x][y] == "\\": # 0 <-> 3 / 1 <-> 2
            x, y, dir_num = move(x, y, 3 - dir_num)
        
        count += 1
    return count

#시작 위치와 방향
x, y, dir_num = init(k)
count = simulate(x, y, dir_num)
print(count)