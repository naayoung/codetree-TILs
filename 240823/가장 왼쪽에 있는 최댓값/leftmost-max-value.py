n = int(input())
num = list(map(int, input().split()))

answer = []
max_num = max(num)
max_num_index = num.index(max(num)) + 1

while max_num_index > 1:
    max_num = max(num)
    max_num_index = num.index(max(num)) + 1
    answer.append(max_num_index)

    num = num[0:max_num_index-1]
print(*answer)