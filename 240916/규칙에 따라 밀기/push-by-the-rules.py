a = input()
word = list(input())

for i in word:
    if i == "L":
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]
print(a)