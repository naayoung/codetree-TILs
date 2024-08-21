n = int(input())

num = [int(input()) for _ in range(n)]

for i in num:
    if i%2 == 1 and i%3 == 0:
        print(i)