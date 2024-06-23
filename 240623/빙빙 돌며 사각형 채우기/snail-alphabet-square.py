n, m = tuple(map(int, input().split()))

arr = [
    [0] * m for _ in range(n)
]


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

d_dir = 0
x, y = 0, 0

def in_range(x, y):
    return x >= 0 and x<n and y>=0 and y<m 

arr[0][0] = chr(65)
orin = 64
for i in range(2, n*m + 1):

    i = i % 27

    i = orin + i
    
    word = chr(i)

    nx, ny = x+dxs[d_dir], y+dys[d_dir]

    if in_range(nx, ny) and arr[nx][ny] == 0:
        x, y = nx, ny
    
    else:
        d_dir = (d_dir + 1) % 4
        x, y = x+dxs[d_dir], y+dys[d_dir]

    arr[x][y] = word

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()