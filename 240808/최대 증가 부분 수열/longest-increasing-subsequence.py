n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [ -1 for _ in range(n+1) ]
dp[0] = 0

for i in range(1, n+1):
    
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])


print(max(dp))