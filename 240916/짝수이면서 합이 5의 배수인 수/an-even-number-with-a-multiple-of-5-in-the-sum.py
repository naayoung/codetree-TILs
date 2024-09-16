n = list(input())
temp = int(''.join(n))

def pro(temp):
    ans = 0
    for i in n:
        i = int(i)
        ans += i
    return ans%5 == 0 and temp%2 == 0

if pro(temp):
    print('Yes')
else:
    print('No')