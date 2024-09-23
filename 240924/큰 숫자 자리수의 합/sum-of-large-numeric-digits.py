a, b, c = map(int, input().split())

def sol(temp):
    if temp < 10:
        return temp
    return sol(temp//10) + temp%10
    
temp = a*b*c
print(sol(temp))