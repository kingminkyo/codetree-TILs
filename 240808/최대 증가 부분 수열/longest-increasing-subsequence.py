n = int(input())
arr = list(map(int, input().split()))

dp = [ -1 for _ in range(n) ]
dp[0] = 1

for i in range(1, n):
    
    for j in range(0, i):



        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])


result = 0 
for d in dp:
    result = max(result, d)
print(result)