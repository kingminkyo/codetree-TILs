n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def find_max(x, y):
    if dp[x][y] != 0:
        return dp[x][y]

    best = 1


    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            best = max(best, find_max(nx, ny) + 1)


    dp[x][y] = best
    return best

ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, find_max(i, j))

print(ans)