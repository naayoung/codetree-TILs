n = int(input())

def sol1(n):
    if n == 0:
        return
    sol1(n-1)
    print(n, end=' ')

def sol2(n):
    if n == 0:
        return
    print(n, end=' ')
    sol2(n-1)

sol1(n)
print()
sol2(n)