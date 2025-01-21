R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Write your code here!
"""
1. 이동 가능 여부 확인
    1-1. 색상 파악
    1-2. 그리드 안에 위치해있는지 확인
2. 점프 진행 시, 점프 가능한 곳인지 확인 (왼쪽이나 위로 이동은 하지않음)
3. 이동한 위치 2곳인지 확인
4. 만족하는 경우 count
"""
jump_count = 0
ans = 0

for y in range(C):
    for x in range(R):
        currnet_color = grid[x][y]
        jump_count = 0
        for dy in range(y+1, C):
            for dx in range(x+1, R):
                if currnet_color != grid[dx][dy]:
                    jump_count += 1
                    
        if jump_count == 2:
            ans += 1

print(ans)






