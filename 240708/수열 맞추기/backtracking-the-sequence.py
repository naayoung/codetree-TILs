from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

result = deque()
current = 1  # 현재 처리할 값

for op in reversed(a):
    if op == 1:
        # 가장 앞 원소를 처리
        result.appendleft(current)
    elif op == 2:
        # 두 번째 원소를 처리
        if len(result) >= 1:
            result.insert(1, current)
        else:
            result.appendleft(current)
    elif op == 3:
        # 가장 뒤 원소를 처리
        result.append(current)
    current += 1

print(*result)