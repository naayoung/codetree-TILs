A = list(input())

# Write your code here!
ans = []
cnt = 0
for a in A:
    if a == '(':
        ans.append(a)
    elif a == ')' and len(ans) == 0:
        pass
    elif a == ')':
        cnt += 1
        ans.pop()
cnt = cnt - len(ans)
print(cnt)
