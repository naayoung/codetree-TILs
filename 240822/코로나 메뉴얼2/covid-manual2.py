tem = [input().split() for _ in range(3)]

answer = [0] * 4
for t in tem:
    if t[0] == 'Y' and int(t[1]) >= 37:
        answer[0] += 1
    elif t[0] == 'N' and int(t[1]) >= 37:
        answer[1] += 1
    elif t[0] == 'Y' and int(t[1]) < 37:
        answer[2] += 1
    else:
        answer[3] += 1
if answer[0] >= 2:
    answer.append('E')
print(*answer)