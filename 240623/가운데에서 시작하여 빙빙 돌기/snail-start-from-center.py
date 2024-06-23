n = int(input())


arr = [
    [0] * n for _ in range(n)
]

mid = int(n/2 )
x, y = mid, mid 

dxs, dys = [0, -1, 0, 1] , [1, 0, -1, 0]

arr[x][y] = 1

def in_range(x, y):
    return x>= 0 and x<n and y>=0 and y<n

d_dir = 0

for i in range(2, n*n+1):

    dx, dy = x+dxs[d_dir], y+dys[d_dir]

    if in_range(dx, dy) and arr[dx][dy] == 0:
        x, y = dx, dy
        arr[x][y] = i

    ex_dir = (d_dir + 1) % 4
    dx, dy = x+dxs[ex_dir], y+dys[ex_dir]
    
    if in_range(dx, dy) and arr[dx][dy] == 0:
        d_dir = (d_dir + 1) % 4

for i in range(n):
    for j in range(n):
        print(arr[i][j] , end=" ")
    print()