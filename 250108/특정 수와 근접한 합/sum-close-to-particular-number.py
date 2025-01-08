import copy

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
ans = 10000
for i in range(N):
    temp = copy.deepcopy(arr)
    temp.remove(arr[i])
    for j in range(1, N):
        if i != j:
            if len(temp) != N-1:
                temp.append(arr[j-1])
            temp.remove(arr[j])
        if abs(sum(temp) - S) < ans:
            ans = abs(sum(temp) - S)
print(ans)