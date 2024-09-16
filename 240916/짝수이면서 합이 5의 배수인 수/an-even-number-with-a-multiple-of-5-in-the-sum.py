def pro(ans):
    if ans%5 == 0:
        print('Yes')
    else:
        print('No')

n = list(input())
ans = 0
for i in n:
    i = int(i)
    ans += i
pro(ans)