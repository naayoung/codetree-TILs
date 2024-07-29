max_num = 1000
mod = 10007

n = int(input().strip())
dp = [0] * (max_num + 1)

dp[0] = 1 
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n])