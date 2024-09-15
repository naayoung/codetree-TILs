word = list(input())

answer = []
for i in range(len(word)):
    if word[i] == word[1]:
        answer.append(word[0])
    else:
        answer.append(word[i])
print(''.join(answer))