n = int(input())

cnt = 1
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j == i:
            print(cnt, "*", j, "=", cnt*j, end=" ")
        else:
            print(cnt, "*", j, "=", cnt*j, end=" / ")
    cnt += 1
    print()