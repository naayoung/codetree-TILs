n = int(input())

for i in range(1, n+1):
    if i%2 != 0:
        print('* ' * (n-(i-1)//2))
    else:
        print('* ' * (i//2))
for i in range(n, 0, -1):
    if i%2 != 0:
        print('* ' * (n-(i-1)//2))
    else:
        print('* ' * (i//2))