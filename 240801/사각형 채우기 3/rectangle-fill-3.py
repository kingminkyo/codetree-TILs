n = int(input())

dp = [0] * (n+1)

dp[1] = 2
dp[2] = 7

for i in range(3, n):
    dp[i] = (dp[i-1] * 4 - 1) % 1000000007

print(dp[n])