a = input()
b = input()

while True:
    if b in a:
        answer = a.replace(b, "")
        a = answer
    else:
        break
print(answer)