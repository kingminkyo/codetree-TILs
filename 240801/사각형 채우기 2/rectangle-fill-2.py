n = int(input())

dp = [0] * (n+1)

dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = d[i-1] + d[i-2] * 2

print(dp[n])