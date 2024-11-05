n = int(input())
answer = 0

offset = 100
for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    x1, y1, x2, y2 = x1+offset, y1+offset, x2+offset, y2+offset

    answer = (x2-x1)*(y2-y1)
print(answer)