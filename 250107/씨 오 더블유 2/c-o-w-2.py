n = int(input())
str = input()

# Write your code here!
c, o, w = [], [], []
for s in range(len(str)):
    if str[s] == 'C':
        c.append(s+1)
    if str[s] == 'O':
        o.append(s+1)
    if str[s] == 'W':
        w.append(s+1)
print(len(c)*len(o)*len(w))
