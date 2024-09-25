n, k, T = input().split()
n, k = int(n), int(k)

word = []
for _ in range(n):
    temp = input()
    if temp[:len(T)] == T:
        word.append(temp)

word.sort()
print(word[k-1])