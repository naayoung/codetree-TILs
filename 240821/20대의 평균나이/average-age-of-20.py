num = []

while True:
    age = int(input())
    if age < 30 and age >= 20:
        num.append(age)
    else:
        answer = sum(num)/len(num)
        print(f"{answer:.2f}")
        break