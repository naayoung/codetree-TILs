a, b = map(int, input().split())

def sol(a, b):
    if a > b:
        a = a*2
        b = b+10
    else:
        a = a+10
        b = b*2
    return a, b

a, b = sol(a, b)
print(a, b)