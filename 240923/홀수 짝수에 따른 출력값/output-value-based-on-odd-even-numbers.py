n = int(input())

def sol(n):
    if n == 0:
        return 0

    return sol(n-2) + n

print(sol(n))