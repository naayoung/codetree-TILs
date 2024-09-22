n = int(input())
num = list(map(int, input().split()))

def sol(n):
    if n == 0:
        return num[0]
    return max(sol(n-1), num[n])

print(sol(n-1))