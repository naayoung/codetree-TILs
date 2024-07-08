import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
seq = [0 for _ in range(n)]

def is_happy_sequence():
    cnt, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i-1] == seq[i]:
            cnt += 1
        else:
            cnt = 1
        
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt >= m

count = 0
#가로
for i in range(n):
    seq = graph[i][:]

    if is_happy_sequence():
        count += 1

#세로
for j in range(n):
    for i in range(n):
        seq[i] = graph[i][j]
    
    if is_happy_sequence():
        count += 1

print(count)