n = int(input())

answer = [0] * 20
m = 10
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'L':
        m = m-a
    else:
        m = m+a
    answer[m] += 1
print(sum(answer))