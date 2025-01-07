n = int(input())
str = input()

# Write your code here!
c, o, w = [], [], []
for s in range(n):
    if str[s] == 'C':
        c.append(s+1)
    if str[s] == 'O':
        o.append(s+1)
    if str[s] == 'W':
        w.append(s+1)

answer = 0
for cc in c:
    for oo in o:
        if oo > cc:
            for ww in w:
                if ww > oo:
                    answer += 1
print(answer)