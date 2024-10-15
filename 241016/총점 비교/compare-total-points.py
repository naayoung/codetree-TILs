n = int(input())
answer = []
for _ in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    answer.append([name, a, b, c])
answer.sort(key=lambda x:x[1]+x[2]+x[3])

for ans in answer:
    print(*ans)