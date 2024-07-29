max_stair = 1000
mod = 10007

n = int(input().strip())
dp = [0] * (max_stair + 1)

# 초기 조건 설정
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 3]) % MOD

print(dp[n])