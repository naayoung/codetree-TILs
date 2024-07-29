import sys
input = sys.stdin.readline

n = int(input().strip())
max_num = 45

dp = [0 for _ in range(max_num+1)]
dp[1] = dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])