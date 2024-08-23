n, m = map(int, input().split())

answer = [[0]*m for _ in range(n)]

num = 1
#n-1+m-1이 합계의 최대값
for nn in range(n+m-1):
    for i in range(nn+1):
        j = nn - i
        if i < n and j < m:
            answer[i][j] = num
            num += 1

for ans in answer:
    print(*ans)

'''
0, 0

0, 1
1, 0


0, 2
1, 1
2, 0

0, 3
1, 2
2, 1
3, 0

'''