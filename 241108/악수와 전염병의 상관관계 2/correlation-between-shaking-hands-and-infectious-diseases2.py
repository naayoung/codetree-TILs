N, K, P, T = map(int, input().split())

temp = []
for _ in range(T):
    t, x, y = map(int, input().split())
    temp.append((t, x, y))
temp.sort(key = lambda x:x[0])

cnt = [0]*N
people = [0]*N
people[P-1] = 1

for i in temp:
    if people[i[1]-1] == 1 or people[i[2]-1] == 1:
        if people[i[1]-1] == 1 and cnt[i[1]-1] < K:
            cnt[i[1]-1] += 1
            people[i[2]-1] = 1
        elif people[i[2]-1] == 1 and cnt[i[2]-1] < K:
            cnt[i[2]-1] += 1
            people[i[1]-1] = 1

    cnt_temp = 0
    for j in cnt:
        if j >= K:
            cnt_temp += 1
    if cnt_temp == N:
        break

answer = ''
for i in people:
    answer += str(i)
print(answer)