n, m = map(int, input().split())
a = list(map(int, input().split()))

def sol():
    global m

    temp = a[m-1]
    while m > 1:
        if m%2 == 0:
            m = m//2
        else:
            m -= 1
        temp += a[m-1]
    return temp

print(sol())