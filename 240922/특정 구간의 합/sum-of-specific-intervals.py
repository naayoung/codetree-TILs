n, m =map(int, input().split())
num = list(map(int, input().split()))

def sol(a1, a2):
    temp = 0
    for i in range(a1, a2+1):
        temp += num[i-1]
    return temp

for _ in range(m):
    a1, a2 = map(int, input().split())
    answer = sol(a1, a2)
    print(answer)