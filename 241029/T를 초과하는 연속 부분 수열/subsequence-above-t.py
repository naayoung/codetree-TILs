n, t = map(int, input().split())
temp = list(map(int, input().split()))

answer, cnt = 0, 0
for i in range(n):
    if temp[i] > t:
        cnt += 1
    else:
        cnt = 0
    answer = max(cnt, answer)
print(answer)