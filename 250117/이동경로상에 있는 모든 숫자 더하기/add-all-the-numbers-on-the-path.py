N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Write your code here!
"""
초기값: 가운데 위치에서 북쪽을 향한 상태로 움직임
L: 왼쪽으로 90도 방향 회전
R: 오른쪽으로 90도 방향 회전
F: 바라보고 있는 방향 한칸 이동

*시작 위치 포함하여 덧셈
**격자 범위 벗어나면 명령어 무시
"""
#1. 주어진 크기(N)에서 가운데 위치 구하기
    #1-1. 바라보는 방향은 북쪽
#2. 명령어에 따른 방향 변화 함수
#3. 격자 범위 확인

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

#초기값
x, y = N//2, N//2
dir_num = 3
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

#답
ans = board[x][y]

#입력값 읽기
for d in str:
    if d == 'F':
        dx, dy = x+dxs[dir_num] , y+dys[dir_num]
        if in_range(dx, dy):
            x, y = dx, dy
            ans += board[x][y]
    elif d == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif d == 'R':
        dir_num = (dir_num + 1) % 4
print(ans)





