n = int(input())
num = list(map(int, input().split()))

num.sort()
print(num[1]+num[2*n-2])