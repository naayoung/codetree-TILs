n = int(input())
num = list(map(int, input().split()))

# 유클리드 호제법으로 최대공약수를 구하는 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 두 수의 최소공배수를 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 리스트에서 첫 번째부터 끝까지의 최대공약수를 재귀적으로 구하는 함수
def find_gcd_of_list(nums, idx):
    if idx == 0:
        return nums[0]  # 재귀의 기본 경우
    return gcd(nums[idx], find_gcd_of_list(nums, idx - 1))

# 리스트에서 첫 번째부터 끝까지의 최소공배수를 재귀적으로 구하는 함수
def find_lcm_of_list(nums, idx):
    if idx == 0:
        return nums[0]  # 재귀의 기본 경우
    return lcm(nums[idx], find_lcm_of_list(nums, idx - 1))

print(find_lcm_of_list(num, n - 1))