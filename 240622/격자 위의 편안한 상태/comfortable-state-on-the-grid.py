n, m = tuple(map(int, input().split()))

arr = [
    [0]*n for _ in range(n)
]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    arr[x-1][y-1] = 1

    cnt = 0

    for dxs, dys in zip(dx, dy):
        nx, ny  = x-1+dxs, y-1+dys
        if in_range(nx, ny) and arr[nx][ny] ==1:
            cnt+= 1

    if cnt==3:
        print(1)
    else:
        print(0)