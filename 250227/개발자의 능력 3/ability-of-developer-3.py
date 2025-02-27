import sys
abilities = list(map(int, input().split()))

# Please write your code here.
def sum_dev(a, b, c):
    sum1 = abilities[a] + abilities[b] + abilities[c]
    sum2 = sum(abilities) - sum1
    return abs(sum1 - sum2)

ans = sys.maxsize
for a in range(6):
    for b in range(a+1, 6):
        for c in range(b+1, 6):
            ans = min(ans, sum_dev(a, b, c))
print(ans)
