n = int(input())

def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return sol(n-2) + n

print(sol(n))