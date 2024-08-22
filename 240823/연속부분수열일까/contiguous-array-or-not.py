n1, n2 = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if num2 in num1:
    print('Yes')
else:
    print('No')