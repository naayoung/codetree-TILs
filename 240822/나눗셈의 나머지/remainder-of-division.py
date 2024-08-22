a, b = map(int, input().split())

temp = [0] * 10
answer = 0

while a > 1:
    a = a//b
    temp[a%b] += 1

for i in temp:
    answer += i**2
print(answer)