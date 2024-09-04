n = int(input())
word = []
for _ in range(n):
    word.append(input())
temp = input()

for i in word:
    if i[0] != temp:
        word.remove(i)

temp2 = 0
for i in word:
    temp2 += len(i)

print(f"{len(word)}", f"{temp2/len(word):.2f}")