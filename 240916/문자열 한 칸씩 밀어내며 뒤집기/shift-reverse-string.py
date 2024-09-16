word, q = input().split()
q = int(q)

for i in range(q):
    n = int(input())
    if n == 1:
        word = word[1:] + word[0]
        print(word)
    elif n == 2:
        word = word[-1] + word[:-1]
        print(word)
    else:
        word = word[::-1]
        print(word)