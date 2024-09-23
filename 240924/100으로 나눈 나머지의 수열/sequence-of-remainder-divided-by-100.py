n = int(input())

def sol(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (sol(n-1)*sol(n-2))%100

print(sol(n))