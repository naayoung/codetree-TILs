n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
ans = []
for a in arr:
    for i in range(n):
        temp = a[i:i+3]
        if len(temp) == 3:
            ans.append(sum(temp))
ans.sort(reverse=True)
print(ans[0]+ans[1])