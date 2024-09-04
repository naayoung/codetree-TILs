n = int(input())

for _ in range(n):
    answer = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i%2 == 0:
            answer += i
    print(answer)