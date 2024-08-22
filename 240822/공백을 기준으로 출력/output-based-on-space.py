sen = [input().split() for _ in range(2)]

answer = ''
for i in sen:
    for j in i:
        answer += j
print(answer)