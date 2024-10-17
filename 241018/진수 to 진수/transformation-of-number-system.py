a, b = map(int, input().split())
n = list(map(int, input()))
nn = 0
answer = []

#a진수에서 10진수로 변경
for i in range(len(n), 0, -1):
    nn += n[i]*(a**i)

#10진수에서 b진수로 변경
while True:
    if nn < b:
        answer.append(nn)
        break
    answer.append(nn%b)
    nn = nn//b

#출력
for i in answer[::-1]:
    print(i, end="")