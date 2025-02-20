n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
cnt = 0
for i in range(1, n):
    for j in range(i, n):
        t = arr[i:j+1]
        tt = sum(t)//len(t)
        if tt in t:
            cnt += 1
print(cnt)