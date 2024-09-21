a = input()

def check_palindrome(a):
    a = list(a)
    a.reverse()
    a = ''.join(a)
    return a

if check_palindrome(a) == a:
    print('Yes')
else:
    print('No')