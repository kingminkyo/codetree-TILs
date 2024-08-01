n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

min_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

max_arr[0][0], min_arr[0][0], dp[0][0] = arr[0][0], arr[0][0], arr[0][0]

for i in range(1, n):
    max_arr[i][0] = max(max_arr[i-1][0], arr[i][0])
    min_arr[i][0] = min(min_arr[i-1][0], arr[i][0])

    max_arr[0][i] = max(max_arr[0][i-1], arr[0][i])
    min_arr[0][i] = min(min_arr[0][i-1], arr[0][i])

for i in range(1, n):
    for j in range(1, n):
        max_arr[i][j] = max(min(max_arr[i-1][j], max_arr[i][j-1]), arr[i][j])
        min_arr[i][j] = min(max(min_arr[i-1][j], min_arr[i][j-1]), arr[i][j])

for i in range(n):
    for j in range(n):
        dp[i][j] = max_arr[i][j] - min_arr[i][j]

print(dp[n-1][n-1])


def print_arr(x):
    for i in range(n):
        for j in range(n):
            print(x[i][j], end=" ")
        print()
    print()

# print_arr(max_arr)
# print_arr(min_arr)