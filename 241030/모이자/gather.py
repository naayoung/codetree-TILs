import sys

n = int(input())
num = list(map(int, input().split()))

answer = sys.maxsize
#i는 집
for i in range(n):
    temp = 0
    for j in range(n):
        temp += num[j]*abs(j-i)
    answer = min(answer, temp)
print(answer)