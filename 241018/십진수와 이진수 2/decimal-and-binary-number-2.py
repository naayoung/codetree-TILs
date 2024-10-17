n = list(map(int, input()))
nn = 0
answer = []

#10진수
for i in range(len(n)):
    nn = nn*2 + n[i]

#10진수 17배
nn = nn*17

#2진수
while True:
    if nn < 2:
        answer.append(nn)
        break
    answer.append(nn%2)
    nn = nn//2

#출력
for i in answer[::-1]:
    print(i, end="")