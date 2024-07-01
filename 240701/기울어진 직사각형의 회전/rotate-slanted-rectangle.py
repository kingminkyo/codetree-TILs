n = int(input())

arr =[
    list(map(int, input().split()))
    for _ in range(n)
]
sub = [
    [0] * n
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        sub[i][j] = arr[i][j]



r, c, k, l, k, l, d = map(int, input().split())


r, c = r-1, c-1 



def clockwise(r, c, k, l):

    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    
    for i in range(1, k+1):
        nx, ny = r+dxs[0]*i, c+dys[0]*i
        ex, ey = r+dxs[0]*(i-1), c+dys[0]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[0]*k, c+dys[0]*k

    for i in range(1, l+1):
        nx, ny = r+dxs[1]*i, c+dys[1]*i
        ex, ey = r+dxs[1]*(i-1), c+dys[1]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[1]*l, c+dys[1]*l

    for i in range(1, k+1):
        nx, ny = r+dxs[2]*i, c+dys[2]*i
        ex, ey = r+dxs[2]*(i-1), c+dys[2]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[2]*k, c+dys[2]*k

    for i in range(1, l+1):
        nx, ny = r+dxs[3]*i, c+dys[3]*i
        ex, ey = r+dxs[3]*(i-1), c+dys[3]*(i-1)
        arr[nx][ny] = sub[ex][ey]
    
def clock(r, c, k, l):

    dxs, dys = [-1, -1, 1, 1], [-1, 1, 1, -1]
    
    for i in range(1, k+1):
        nx, ny = r+dxs[0]*i, c+dys[0]*i
        ex, ey = r+dxs[0]*(i-1), c+dys[0]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[0]*k, c+dys[0]*k

    for i in range(1, l+1):
        nx, ny = r+dxs[1]*i, c+dys[1]*i
        ex, ey = r+dxs[1]*(i-1), c+dys[1]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[1]*l, c+dys[1]*l

    for i in range(1, k+1):
        nx, ny = r+dxs[2]*i, c+dys[2]*i
        ex, ey = r+dxs[2]*(i-1), c+dys[2]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[2]*k, c+dys[2]*k

    for i in range(1, l+1):
        nx, ny = r+dxs[3]*i, c+dys[3]*i
        ex, ey = r+dxs[3]*(i-1), c+dys[3]*(i-1)
        arr[nx][ny] = sub[ex][ey]

if d == 0:
    clockwise(r, c, k, l)
else:
    clock(r, c, k, l)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()