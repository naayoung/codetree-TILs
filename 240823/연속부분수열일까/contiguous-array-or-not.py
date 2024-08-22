n1, n2 = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

cnt = 0
for n in range(n1-n2+1):
    if num1[n:n+n2] == num2:
        cnt += 1

if cnt >= 1:
    print('Yes')
else:
    print('No')