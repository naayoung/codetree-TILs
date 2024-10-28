n = int(input())
temp = [int(input()) for _ in range(n)]
answer, cnt = 0, 0
for i in range(n):
    if (temp[i] > 0 and temp[i-1] > 0) or (temp[i] < 0 and temp[i-1] < 0):
        cnt += 1
    else:
        cnt = 1
    answer = max(cnt, answer)
print(answer)