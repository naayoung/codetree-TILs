n = int(input())
word = []
for _ in range(n):
    word.append(input())
temp = input()

word2 = []
for i in word:  
    if i[0] == temp:
        word2.append(i)
temp2 = 0
for i in word2:
    temp2 += len(i)

print(len(word2), f"{temp2/len(word2):.2f}")