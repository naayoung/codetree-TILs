n = int(input())
num = list(map(int, input().split()))

answer = []
while True:
    max_num = max(num)
    max_num_index = num.index(max(num)) + 1
    answer.append(max_num_index)

    num = num[0:max_num_index-1]

    if max_num_index == 1:
        break
print(*answer)