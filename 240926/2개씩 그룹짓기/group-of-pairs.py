n = int(input())
num = list(map(int, input().split()))

num.sort()
num.pop(0)
num.pop(-1)

print(num[0]+num[-1])