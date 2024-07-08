import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
num = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if num[i] + num[j] == m:
            count += 1
print(count)