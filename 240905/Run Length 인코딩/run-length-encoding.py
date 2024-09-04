word = input()

temp = word[0]
cnt = 0
answer = []
for i in range(len(word)):
    if temp == word[i]:
        cnt += 1
    elif temp != word[i]:
        answer.append(temp)
        answer.append(str(cnt))

        temp = word[i]
        cnt = 1

answer.append(temp)
answer.append(str(cnt))

answer_final = ''.join(answer)

print(len(answer_final))
print(answer_final)