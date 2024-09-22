n = int(input())

answer = 0
def sol(n):
    global answer
    if n == 0:
        print(answer)
        return
    answer += n
    sol(n-1)

sol(n)