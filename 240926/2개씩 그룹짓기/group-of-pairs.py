n = int(input())
num = list(map(int, input().split()))

answer = []
for i in range(n):
    temp = num[i] + num[i+1]
    answer.append(temp)
answer.sort()
if len(answer)%2 == 0:
    print(answer[len(answer)//2-1])
else:
    print(answer[len(answer)//2])