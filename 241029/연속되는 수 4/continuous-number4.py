n = int(input())
temp = [int(input()) for _ in range(n)]

answer, cnt = 0, 0
for i in range(n):
    if i >= 1 and temp[i] > temp[i-1]:
        cnt += 1
    else:
        cnt = 1
    answer = max(cnt, answer)
print(answer)