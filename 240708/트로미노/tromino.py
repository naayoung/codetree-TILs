import sys
input = sys.stdin.readline

#입력값
n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]

# 블록 패턴 정의
block1_patterns = [
    [(0, 0), (0, 1), (0, 2)],  # 1x3 수평
    [(0, 0), (1, 0), (2, 0)]   # 3x1 수직
]
block2_patterns = [
    [(0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (0, 1), (1, 0)]
]

def calculate_max_sum(patterns):
    max_sum = 0
    for pattern in patterns:
        for j in range(m):
            for i in range(n):
                current_sum = 0
                valid = True
                for dx, dy in pattern:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        current_sum += graph[ni][nj]
                    else:
                        valid = False
                        break
                if valid:
                    max_sum = max(max_sum, current_sum)
    return max_sum

# 블록1과 블록2의 최대 합 계산
max_block1_sum = calculate_max_sum(block1_patterns)
max_block2_sum = calculate_max_sum(block2_patterns)

# 전체 최대값 출력
print(max(max_block1_sum, max_block2_sum))