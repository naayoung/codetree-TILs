num = list(map(int, input().split()))

for i in range(2, 10):
    temp = num[i-1] + 2*num[i-2]
    num.append(temp)
print(*num)