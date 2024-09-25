n = int(input())
nums = list(map(int, input().split()))

answer = []
for i in range(n):
    if i%2 == 0:
        temp = nums[:i+1]
        temp.sort()
        answer.append(temp[len(temp)//2])
print(*answer)