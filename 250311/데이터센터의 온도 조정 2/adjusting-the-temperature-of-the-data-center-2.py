N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def work(A, a, b):
    if A < a:
        return C
    elif A >= a and A <= b:
        return G
    elif A > b:
        return H

def work_sum(A):
    total = 0
    for i in range(N):
        a, b = ranges[i][0], ranges[i][1]
        total += work(A, a, b)
    return total

ans = 0
for A in range(10001):
    ans = max(ans, work_sum(A))
print(ans)