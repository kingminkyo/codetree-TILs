n = int(input())

dp = [0] * (n+2)

dp[0] = 1
dp[1] = 1

for i in range(2, n):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp(n))