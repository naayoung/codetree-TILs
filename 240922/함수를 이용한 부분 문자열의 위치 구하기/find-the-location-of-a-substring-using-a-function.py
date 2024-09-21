a = input()
b = input()

def sol(a, b):
    if b in a:
        for i in range(len(a)):
            temp = a[i:i+len(b)]
            if temp == b:
                return i
    else:
        return -1

print(sol(a, b))