N, K, P, T = map(int, input().split())

temp = []
for _ in range(T):
    t, x, y = map(int, input().split())
    temp.append((t, x, y))
temp.sort(key = lambda x:x[0])

cnt = 0
people = [0]*N
people[P-1] = 1
for i in temp:
    if not (people[i[1]-1] == 1 and people[i[2]-1] == 1) and (people[i[1]-1] == 1 or people[i[2]-1] == 1):
        cnt += 1
        people[i[1]-1] = 1
        people[i[2]-1] = 1
        
        if cnt == K:
            break

answer = ''
for i in people:
    answer += str(i)
print(answer)