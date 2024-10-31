n = int(input())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(n-2):
        tmp = num[i][j]+num[i][j+1]+num[i][j+2]
        cnt = max(cnt, tmp)
print(cnt)