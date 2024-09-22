n = int(input())

def sol(n):
    global cnt

    if n == 1:
        return cnt
    cnt += 1
    if n%2 == 0:
        return sol(n//2)
    else:
        return sol(n//3)
    
cnt = 0
print(sol(n))