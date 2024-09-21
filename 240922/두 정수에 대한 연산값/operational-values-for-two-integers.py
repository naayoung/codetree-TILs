a, b = map(int, input().split())

if a > b:
    a = a+25
    b = b*2
else:
    a = a*2
    b = b+25

print(a, b)