import sys

dev = list(map(int, input().split()))
n = 5
ans = sys.maxsize

def sum_dev(a, b, c, d):
    temp = []
    sum1 = dev[a]+dev[b]
    sum2 = dev[c]+dev[d]
    sum3 = sum(dev)-sum1-sum2

    if sum1 != sum2 != sum3:
        temp.append(sum1)
        temp.append(sum2)
        temp.append(sum3)

    return temp



for a in range(n):
    for b in range(a+1, n):
        for c in range(n):
            for d in range(c+1, n):
                if c == a or c == b or d == a or d == b:
                    continue
                temp = sum_dev(a, b, c, d)
                if temp:
                    ans = min(ans, max(temp)-min(temp))
print(ans)


        