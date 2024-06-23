n, m = tuple(map(int, input().split()))

arr = [
    [0] * m for _ in range(n)
]

arr[0][0] = 1

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

d_dir = 0
x, y = 0, 0

for i in range(2, m*n+1):
    x, y = x+dxs[d_dir], y+dys[d_dir]

    if not in_range(x+dxs[d_dir], y+dys[d_dir]) or arr[x+dxs[d_dir]][y+dys[d_dir]] != 0:
        d_dir = (d_dir + 1) % 4

    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()