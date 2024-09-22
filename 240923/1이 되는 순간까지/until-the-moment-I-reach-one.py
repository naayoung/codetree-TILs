n = int(input())

def sol(n):
    if n == 1:
        return 0

    if n%2 == 0:
        return sol(n//2) + 1
    else:
        return sol(n//3) + 1
    
print(sol(n))