n = int(input())
numbers = list(map(int, input().split()))

# Write your code here!
nn = len(numbers)
max_sum = 0

for i in range(nn):
    for j in range(nn):
        if i == j:
            pass
        else:
            if max_sum <= numbers[i]+numbers[j] and abs(i-j) != 1:
                max_sum = numbers[i]+numbers[j]

print(max_sum)


