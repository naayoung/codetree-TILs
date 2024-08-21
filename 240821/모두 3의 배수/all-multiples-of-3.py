num = [int(input()) for _ in range(5)]

answer = True
for i in num:
    if i%3 != 0:
        answer = False
if answer:
    print(1)
else:
    print(0)