import sys
input = sys.stdin.readline

n, t = tuple(map(int, input().split()))
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = list(map(int, input().split()))

for _ in range(t):
    #num1의 마지막 수 temp
    temp = num1[n-1]
    #num1 이동 및 첫번째 수 넣기
    for i in range(n-1, 0, -1):
        num1[i] = num1[i-1]
    num1[0] = num3[n-1]

    #num3 이동
    for i in range(n-1, 0, -1):
        num3[i] = num3[i-1]
    #num3 첫번째 수 넣기
    num3[0] = num2[n-1]

    #num2 이동 및 첫번째 수 넣기
    for i in range(n-1, 0, -1):
        num2[i] = num2[i-1]
    num2[0] = temp

print(*num1)
print(*num2)
print(*num3)