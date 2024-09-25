n = int(input())
num = list(map(int, input().split()))

num.sort()
max_sum = 0

while num:
    num1 = num.pop(0)
    num2 = num.pop(-1)

    num_sum = num1 + num2

    if num_sum > max_sum:
        max_sum = num_sum
print(max_sum)