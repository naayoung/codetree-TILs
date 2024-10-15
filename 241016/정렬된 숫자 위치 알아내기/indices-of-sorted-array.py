n = int(input())
num = list(map(int, input().split()))
new_num = sorted(num)

answer = []
for i in range(n):
    t = new_num.index(num[i])
    answer.append(t+1)
    num[i] = 0
    new_num[t] = 0

print(*answer)