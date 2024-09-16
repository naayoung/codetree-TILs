word = list(input())
answer = []
for i in word:
    if i >= 'A' and i <= 'Z':
        answer.append(i.lower())
    else:
        answer.append(i.upper())
print(''.join(answer))