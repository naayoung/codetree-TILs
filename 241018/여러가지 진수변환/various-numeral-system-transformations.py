n, b = map(int, input().split())
answer = []

#b진수로 변경
while True:
    if n < b:
        answer.append(str(n))
        break
    answer.append(str(n%b))
    n = n//b

#출력
for ans in answer[::-1]:
    print(ans, end="")