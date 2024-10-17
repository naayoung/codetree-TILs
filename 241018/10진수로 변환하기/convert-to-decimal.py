n = list(map(int, input()))
answer = 0

for i in range(len(n)):
    answer = answer*2 + n[i]
print(answer)