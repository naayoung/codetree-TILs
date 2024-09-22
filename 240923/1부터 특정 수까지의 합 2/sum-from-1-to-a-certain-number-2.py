n = int(input())

answer = 0
def sol(n):
    if n == 0:
        return 0
    
    return sol(n - 1) + n

print(sol(n))