X, Y = map(int, input().split())

# Please write your code here.
ans = 0
for n in range(X, Y+1):
    number = list(map(int, list(str(n))))
    ans = max(ans, sum(number))
print(ans)