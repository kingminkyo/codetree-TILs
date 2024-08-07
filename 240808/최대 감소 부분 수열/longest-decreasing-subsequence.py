import sys

n = int(input())
arr = [sys.maxsize] + list(map(int, input().split()))
dp = [-1 for _ in range(n+1)]

dp[0] = 0
for i in range(1, n+1):
    for j in range(0, i):

        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
# print(dp)
print(max(dp))