n = int(input())
answer = []
for i in range(n):
    h, w = map(int, input().split())
    answer.append([h, w, i+1])

answer.sort(key=lambda x:(x[0], -x[1]))
for ans in answer:
    print(*ans)