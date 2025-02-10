n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Write your code here!
big_socre = 0
for i in range(1, 10000-k+1):
    score = 0
    for j in range(i, i+k+1):
        if j in x:
            tmp = x.index(j)
            if c[tmp] == 'G':
                score += 1
            else:
                score += 2
    big_socre = max(score, big_socre)
print(big_socre)
