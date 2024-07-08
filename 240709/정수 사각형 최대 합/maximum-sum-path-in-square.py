n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[0][i] = arr[0][i] + dp[0][i-1]
    dp[i][0] = arr[i][0] + dp[i-1][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1] + arr[i][j], dp[i-1][j]+arr[i][j])


result = 0
for i in range(n):
    result = max(dp[n-1][i], result)

print(result)