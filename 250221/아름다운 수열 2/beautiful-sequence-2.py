N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!
B.sort()
cnt = 0
for i in range(N-M+1):
    temp = A[i:i+M]
    temp.sort()
    if temp == B:
        cnt += 1
print(cnt)