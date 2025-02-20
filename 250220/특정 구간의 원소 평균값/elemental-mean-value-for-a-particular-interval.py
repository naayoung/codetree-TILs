n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
cnt = 0
for i in range(n):
    for j in range(i, n):
        t = arr[i:j+1]
        avg = sum(t)/len(t)

        if avg in t:
            cnt += 1

print(cnt)