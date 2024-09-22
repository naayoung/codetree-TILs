n = int(input())

def sol(n):
    if n == 0:
        return
    print(n, end = ' ')
    sol(n-1)
    print(n, end = ' ')
sol(n)