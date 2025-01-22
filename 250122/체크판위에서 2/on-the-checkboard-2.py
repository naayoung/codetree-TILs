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
cnt = 0

# 각 사각형의 꼭지점을 찾아 색상이 모두 다를 때마다 카운트
for i in range(1, R):
    for j in range(1, C):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if grid[0][0] != grid[i][j] and grid[i][j] != grid[k][l] and grid[k][l] != grid[R - 1][C - 1]:
                    cnt += 1
                        
print(cnt)