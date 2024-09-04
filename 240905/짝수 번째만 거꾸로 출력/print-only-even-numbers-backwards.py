word = input()

temp = []
for i in range(len(word)):
    if i%2 != 0:
        temp.append(word[i])
temp.reverse()
print(''.join(temp))