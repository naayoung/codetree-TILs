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
            if people[i[2]-1] == 1:
                cnt[i[1]-1] += 1
                cnt[i[2]-1] += 1
            else:
                cnt[i[1]-1] += 1
                people[i[2]-1] = 1
             
        elif people[i[2]-1] == 1 and cnt[i[2]-1] < K:
            if people[i[1]-1] == 1:
                cnt[i[1]-1] += 1
                cnt[i[2]-1] += 1
            else:
                cnt[i[2]-1] += 1
                people[i[1]-1] = 1 

answer = ''
for i in people:
    answer += str(i)
print(answer)