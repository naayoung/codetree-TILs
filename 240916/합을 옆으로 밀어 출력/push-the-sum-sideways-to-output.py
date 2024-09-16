n = int(input())

answer = 0
for i in range(n):
    num = int(input())
    answer += num
answer = str(answer)
answer = answer[1:] + answer[0]
print(answer)