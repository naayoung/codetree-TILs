n = int(input())
answer = []
for i in range(n):
    x, y = map(int, input().split())
    answer.append([x, y, i+1])
answer.sort(key=lambda x:(x[0]+x[1], x[2]))

for ans in answer:
    print(ans[2])