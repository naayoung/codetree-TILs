A = list(input())

# Write your code here!   

cnt = 0
for i in range(1, len(A)):
    if A[i-1] == '(' and A[i] == '(':
        for j in range(i+2, len(A)):
            if A[j-1] == ')' and A[j] == ')':
                cnt += 1

print(cnt)
