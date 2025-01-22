A = input()

# Write your code here!
aa = len(A)

ans = [0]
temp = 0
for i in range(aa):
    if A[i] == '1':
        temp += 2**abs(i-(aa-1))

for i in range(1, aa):
    tmp = temp
    if A[i] == '1':
        tmp = temp - 2**abs(i-(aa-1))
    else:
        tmp = temp + 2**abs(i-(aa-1))
    ans.append(tmp)
print(max(ans))
