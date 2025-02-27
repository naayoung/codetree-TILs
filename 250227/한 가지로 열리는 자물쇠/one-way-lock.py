N = int(input().strip())
a, b, c = map(int, input().split())

ans = 0
for x in range(1, N+1):
    for y in range(1, N+1):
        for z in range(1, N+1):
            if abs(x-a) <= 2 or abs(y-b) <= 2 or abs(z-c) <= 2:
                ans += 1
print(ans)