from collections import deque

n = int(input())
a = deque([int(input()) for _ in range(n)])

# Write your code here!
ans = []
for _  in range(n):
    temp = 0
    for i in range(n):
        temp += a[i]*i
    ans.append(temp)
    a.rotate(-1)
print(min(ans))
