n = int(input())

dp = [0] * (n+3)

dp[1] = 2
dp[2] = 7

for i in range(3, n+1):
    dp[i] = (dp[i-1] * 3 + 1 ) % 1000000007

print(dp[n])