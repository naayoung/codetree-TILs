a, b = map(int, input().split())

for i in range(2, 9, 2):
    for j in range(b, a-1, -1):
        if j == a:
            print(j,"*",i,"=",j*i, end="")
        else:
            print(j,"*",i,"=",j*i, end=" / ")
    print()