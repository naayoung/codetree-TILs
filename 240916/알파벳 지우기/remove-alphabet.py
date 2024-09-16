w1 = input().upper()
w2 = input().upper()

answer1 = []
answer2 = []
for i in w1:
    if i >= '0' and i <= '8':
        answer1.append(i)
answer1 = int(''.join(answer1))

for i in w2:
    if i >= '0' and i <= '8':
        answer2.append(i)
answer2 = int(''.join(answer2))

print(answer1 + answer2)