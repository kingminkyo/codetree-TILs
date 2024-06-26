n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]



def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m


def rolling(x, y):
    result = 0
    ex = 0
    if in_range(x-1, y-1):
        ex = arr[x][y] + arr[x][y-1] + arr[x-1][y]
        result = max(result, ex)
    if in_range(x-1, y+1):
        ex =arr[x][y] + arr[x][y+1] + arr[x-1][y]
        result = max(result, ex)
    if in_range(x+1, y-1):
        ex =arr[x][y] + arr[x][y-1] + arr[x+1][y]
        result = max(result, ex)
    if in_range(x+1, y+1):
        ex = arr[x][y] + arr[x][y+1] + arr[x+1][y]
        result = max(result, ex)
    if in_range(x-1, y) and in_range(x+1, y):
        ex = arr[x][y] + arr[x-1][y] + arr[x+1][y]
        result = max(result, ex)
    if in_range(x, y-1) and in_range(x, y+1):
        ex = arr[x][y] + arr[x][y-1] + arr[x][y+1]
        result = max(result, ex)

    return result

real = 0 

for i in range(n):
    for j in range(m):
        res = rolling(i, j)
        real = max(real, res)

print(real)