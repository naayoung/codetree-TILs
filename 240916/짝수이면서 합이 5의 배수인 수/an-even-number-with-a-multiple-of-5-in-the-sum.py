def pro(ans, temp):
    if ans%5 == 0 and temp%2 == 0:
        print('Yes')
    else:
        print('No')

n = list(input())
ans = 0
for i in n:
    i = int(i)
    ans += i
temp = int(''.join(n))
pro(ans, temp)