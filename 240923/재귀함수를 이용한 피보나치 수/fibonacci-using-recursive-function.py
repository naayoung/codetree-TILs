n = int(input())

def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return sol(n-1) + sol(n-2)

print(sol(n))