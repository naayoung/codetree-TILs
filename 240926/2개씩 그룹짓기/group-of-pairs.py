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

'''
group_max = 0
for i in range(n):
    # i번째와 2n - 1 - i번째 원소를 매칭합니다.
    group_sum = nums[i] + nums[2*n - 1 - i]
    if group_sum > group_max:
        # 최댓값을 갱신합니다.
        group_max = group_sum

print(group_max)
'''