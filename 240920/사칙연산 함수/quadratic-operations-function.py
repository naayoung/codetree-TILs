a, o, c = input().split()
a, c = int(a), int(c)

temp = ['+', '-', '/', '*']

if o in temp:
    if o == temp[0]:
        print(a, o, c, '=', a+c)
    if o == temp[1]:
        print(a, o, c, '=', a-c)
    if o == temp[2]:
        print(a, o, c, '=', a//c)
    if o == temp[3]:
        print(a, o, c, '=', a*c)
else:
    print('False')