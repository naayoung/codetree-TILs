a = input()

def confirm(a):
    a = list(a)

    temp = []
    for i in a:
        if i not in temp:
            temp.append(i)

    if len(temp) >= 2:
        return True
    else:
        return False

if confirm(a):
    print('Yes')
else:
    print('No')