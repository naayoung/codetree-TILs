n = int(input())

def sol(n, a, b, i):
    if n == i:
        return (a*b)%100
    if n == 1:
        return 2
    if n == 2:
        return 4
    return sol(n, b, (a*b)%100, i+1)

print(sol(n, 2, 4, 3))