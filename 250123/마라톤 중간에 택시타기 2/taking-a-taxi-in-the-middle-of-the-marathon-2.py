n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
ans = []
for i in range(1, n-1):
    ax, ay = x[0], y[0]
    temp = 0
    for j in range(1, n):
        if i != j:
            temp += abs(ax-x[j]) + abs(ay-y[j])
            ax, ay = x[j], y[j]

    ans.append(temp)

print(min(ans))
