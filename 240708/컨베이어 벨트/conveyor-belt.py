import sys
input = sys.stdin.readline

n, t = tuple(map(int, input().split()))
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num2.reverse()

for _ in range(t):
    temp1, temp2 = num1[n-1], num2[0]

    #num1
    for i in range(n-1, 0, -1):
        num1[i] = num1[i-1]
    num1[0] = temp2

    #num2
    for i in range(1, n):
        num2[i-1] = num2[i]
    num2[n-1] = temp1

num2.reverse()
print(*num1)
print(*num2)