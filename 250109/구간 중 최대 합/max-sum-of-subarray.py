n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
ans = 0
for i in range(n):
    for j in range(i+k, n, k):
        temp = arr[i:j]
        ans = max(ans, sum(temp))
print(ans)
