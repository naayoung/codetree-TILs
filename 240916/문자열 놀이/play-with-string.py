s, q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    x, y, z = input().split()
    x = int(x)

    if x == 1:
        y, z = int(y), int(z)
        s[y-1], s[z-1] = s[z-1], s[y-1]
        print(''.join(s))
    else:
        answer = []
        for i in s:
            temp = i.replace(y, z)
            answer.append(temp)
        s = answer
        print(''.join(s))