n = int(input())

def sol(n):
    if n == 0:
        return
    print('* ' * n, end = " ")
    print()
    sol(n-1)
    print('* ' * n, end = " ")
    print()

sol(n)