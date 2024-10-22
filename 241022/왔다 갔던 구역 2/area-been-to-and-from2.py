n = int(input())

answer = [0] * 20
m = 10
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'L':
        for i in range(m-a, m+1):
            answer[i] += 1
    else:
        for i in range(m, m+a+1):
            answer[i] += 1
print(max(answer))