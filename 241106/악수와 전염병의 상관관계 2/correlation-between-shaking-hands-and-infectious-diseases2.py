N, K, P, T = map(int, input().split())

temp = []
for _ in range(T):
    t, x, y = map(int, input().split())
    temp.append((t, x, y))
temp.sort(key = lambda x:x[0])

cnt = 0
people = [0]*N
for i in temp:
    if i[1] == P or i[2] == P:
        cnt += 1
        if cnt == T:
            break
        people[i[1]-1] = 1
        people[i[2]-1] = 1

answer = ''
for i in people:
    answer += str(i)
print(answer)