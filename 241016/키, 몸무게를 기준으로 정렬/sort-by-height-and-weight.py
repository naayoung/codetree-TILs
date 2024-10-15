n = int(input())
answer = []
for _ in range(n):
    n, h, k = input().split()
    h, k = int(h), int(k)
    answer.append([n, h, k])
answer.sort(key=lambda x:(x[1], -x[2]))

for ans in answer:
    print(*ans)