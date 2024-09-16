def answer(n):
    temp = 0
    for i in range(1, n+1):
        temp += i
    return temp//10

n = int(input())
ans = answer(n)
print(ans)