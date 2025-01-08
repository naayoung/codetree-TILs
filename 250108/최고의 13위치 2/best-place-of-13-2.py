n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
ans = []
for a in arr:
    t = 0
    for i in range(n):
        temp = a[i:i+3]
        if len(temp) == 3 and sum(temp) >= 0:
            t = sum(temp)
    ans.append(t)
ans.sort(reverse=True)
print(ans[0]+ans[1])