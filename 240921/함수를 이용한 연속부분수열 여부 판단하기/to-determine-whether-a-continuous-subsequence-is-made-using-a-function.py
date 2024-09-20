n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def sol(A, B, n1, n2):
    cnt = 0
    for i in range(n1-n2-1):
        if A[i:i+n2] == B:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

if sol(A, B, n1, n2):
    print('Yes')
else:
    print('No')