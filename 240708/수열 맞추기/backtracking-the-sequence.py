import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

answer = [0] * n
count = 0

for i in a:
    count += 1
    if i == 1:
        for j in range(n):
            if answer[j] == 0:
                answer[j] = count
                break
    elif i == 2:
        for j in range(1, n):
            if answer[j] == 0:
                answer[j] = count
                break
    else:
        answer.append(count)
answer.reverse()
print(*answer)