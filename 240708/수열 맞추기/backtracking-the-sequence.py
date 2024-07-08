import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

answer = []
count = 0

for i in reversed(a):
    count += 1
    if i == 1:
        answer.insert(0, count)
    elif i == 2:
        answer.insert(1, count)
    else:
        answer.append(count)
print(*answer)