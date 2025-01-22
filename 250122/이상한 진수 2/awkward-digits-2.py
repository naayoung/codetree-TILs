A = input()

# Write your code here!
aa = len(A)

ans = []
temp = 0
for i in range(aa):
    if A[i] == '1':
        temp += 2**abs(i-3)

for i in range(1, aa):
    tmp = temp
    if A[i] == '1':
        tmp = temp - 2**abs(i-3)
    else:
        tmp = temp + 2**abs(i-3)
    ans.append(tmp)
print(max(ans))
