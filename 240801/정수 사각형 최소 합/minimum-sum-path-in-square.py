n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 끝 채우기 
n -= 1
visited[0][n] = arr[0][n]

for i in range(n-1, -1, -1): # 1 0 
    visited[0][i] = visited[0][i+1] + arr[0][i]

for i in range(1, n+1):
    visited[i][n] = visited[i-1][n] + arr[i][n]


n = n+1 
for i in range(1, n):
    for j in range(n-2, -1, -1):
        visited[i][j] = min(visited[i-1][j], visited[i][j+1]) + arr[i][j]

# print(visited)
print(visited[n-1][0])