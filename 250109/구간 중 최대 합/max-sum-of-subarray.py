n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
ans = 0
for i in range(n):
    temp = arr[i:i+k]
    if len(temp) == k:
        ans = max(ans, sum(temp))
print(ans)
