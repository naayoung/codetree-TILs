n = int(input())
word = []
for _ in range(n):
    word.append(input())
temp = input()

for i in word:
    if temp not in i:
        word.remove(i)

temp2 = 0
for i in word:
    temp2 += len(i)

print(len(word), f"{temp2/len(word):.2f}")