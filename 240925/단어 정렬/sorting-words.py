n = int(input())
word = []
for _ in range(n):
    word.append(input())

word.sort()

for i in word:
    print(i)