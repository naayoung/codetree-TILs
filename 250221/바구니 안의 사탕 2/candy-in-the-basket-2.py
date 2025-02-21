N, K = map(int, input().split())
candy = []
pos = [0]*101

for _ in range(N):
    c, p = map(int, input().split())
    pos[p] += c
# Write your code here!
ans = 0
for c in range(101-K):
    temp = pos[c-K:c+K+1]
    if ans < sum(temp):
        ans = sum(temp)
print(ans)

