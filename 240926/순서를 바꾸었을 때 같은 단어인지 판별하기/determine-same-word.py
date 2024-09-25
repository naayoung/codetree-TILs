a = input()
b = input()

a, b = list(a), list(b)
a.sort()
b.sort()

a, b = ''.join(a), ''.join(b)

if a == b:
    print('Yes')
else:
    print('No')