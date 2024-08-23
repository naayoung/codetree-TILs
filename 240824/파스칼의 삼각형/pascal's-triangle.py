n = int(input())

answer = []
for i in range(n):
    row = [1] * (i + 1)

    for j in range(1, i):
        row[j] = answer[i - 1][j - 1] + answer[i - 1][j]

    answer.append(row)

for ans in answer:
    print(*ans)