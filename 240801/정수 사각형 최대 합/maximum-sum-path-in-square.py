n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 0행 0열 채우기 
visited[0][0] = arr[0][0]

for i in range(1, n):
    visited[i][0] = arr[i][0] + visited[i-1][0]
    visited[0][i] = arr[0][i] + visited[0][i-1]

# 점화시키기 
for i in range(1, n):
    for j in range(1, n):
        visited[i][j] = max(visited[i-1][j], visited[i][j-1]) + arr[i][j]

print(visited[n-1][n-1])