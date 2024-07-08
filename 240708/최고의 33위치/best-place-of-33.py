import sys
input = sys.stdin.readline

n = int(input().strip())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def get_num_of_gold(i, j, max_i, max_j):
    cnt = 0
    for c in range(j, max_j+1):
        for r in range(i, max_i+1):
            cnt += graph[r][c]

    return cnt

max_cnt = 0
for j in range(n):
    for i in range(n):
        #범위 체크
        if i+2 >= n or j+2 >= n:
            continue
        #갯수 구하기
        cnt = get_num_of_gold(i, j, i+2, j+2)
        #최대갯수 구하기
        max_cnt = max(max_cnt, cnt)

print(max_cnt)