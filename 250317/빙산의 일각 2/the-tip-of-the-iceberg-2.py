n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
ans = 0

for i in range(1, 1000):
    cnt = 0

    if h[0] > i:
        cnt += 1
    
    for j in range(1, n):
        if h[j] > i and h[j-1] <= i:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
    