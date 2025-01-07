n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
"""
1. arr에서 3개를 고른다
2. 3개 값을 자리 수 별로 더한다
    2-1. 더하면서 10이 넘어가면 -1을 저장
    2-2. 넘어가지 않으면 3개 숫자 합 저장
3. 저장된 값 중 max값 출력
"""
arr.sort()
nlist = []
answer = []
temp = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            nlist.append([arr[i], arr[j], arr[k]])

for nn in nlist:
    a, b, c = str(nn[0]), str(nn[1]), str(nn[2])
    ans = 1
    for i in range(5):
        temp = 0
        if len(a) > i:
            temp += int(a[::-1][i])
            #print(nn, i, a[::-1], temp)
        if len(b) > i:
            temp += int(b[::-1][i])
            #print(nn, i, b[::-1], temp)
        if len(c) > i:
            temp += int(c[::-1][i])
            #print(nn, i, c[::-1], temp)

        if temp >= 10:
            ans = 0
            break
    if ans == 0:
        answer.append(-1)
    else:
        answer.append(sum(nn))
    
print(max(answer))
