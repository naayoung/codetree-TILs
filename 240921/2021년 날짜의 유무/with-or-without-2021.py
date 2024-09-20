M, D = map(int, input().split())

def cal(M, D):
    if M > 12 or D > 31:
        return False
    elif M == 2 and D >= 28:
        return False
    elif M%2 == 0 and D == 31:
        return False
    else:
        return True

if cal(M, D):
    print('Yes')
else:
    print('No')