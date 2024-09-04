n = int(input())

cnt = 0
for i in range(1, n+1):
    for j in range(n):
        #홀수
        if i%2 == 1:
            if i > 1 and j == 0:
                cnt = cnt*2 - 1
            else:
                cnt += 1
        #짝수
        else:
            if j == 0:
                cnt = cnt*2
            else:
                cnt -= 1
        print(cnt, end=" ")
    print()