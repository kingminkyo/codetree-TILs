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



r, c, m1, m2, m3, m4, d = map(int, input().split())


r, c = r-1, c-1 



def clockwise(r, c, m1, m2, m3, m4):

    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    
    for i in range(1, m1+1):
        nx, ny = r+dxs[0]*i, c+dys[0]*i
        ex, ey = r+dxs[0]*(i-1), c+dys[0]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[0]*m1, c+dys[0]*m1

    for i in range(1, m2+1):
        nx, ny = r+dxs[1]*i, c+dys[1]*i
        ex, ey = r+dxs[1]*(i-1), c+dys[1]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[1]*m2, c+dys[1]*m2

    for i in range(1, m3+1):
        nx, ny = r+dxs[2]*i, c+dys[2]*i
        ex, ey = r+dxs[2]*(i-1), c+dys[2]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[2]*m3, c+dys[2]*m3

    for i in range(1, m4+1):
        nx, ny = r+dxs[3]*i, c+dys[3]*i
        ex, ey = r+dxs[3]*(i-1), c+dys[3]*(i-1)
        arr[nx][ny] = sub[ex][ey]
    
def clock(r, c, m1, m2, m3, m4):

    dxs, dys = [-1, -1, 1, 1], [-1, 1, 1, -1]
    
    for i in range(1, m2+1):
        nx, ny = r+dxs[0]*i, c+dys[0]*i
        ex, ey = r+dxs[0]*(i-1), c+dys[0]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[0]*m2, c+dys[0]*m2

    for i in range(1, m1+1):
        nx, ny = r+dxs[1]*i, c+dys[1]*i
        ex, ey = r+dxs[1]*(i-1), c+dys[1]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[1]*m1, c+dys[1]*m1

    for i in range(1, m2+1):
        nx, ny = r+dxs[2]*i, c+dys[2]*i
        ex, ey = r+dxs[2]*(i-1), c+dys[2]*(i-1)
        arr[nx][ny] = sub[ex][ey]

    r, c = r+dxs[2]*m2, c+dys[2]*m2

    for i in range(1, m1+1):
        nx, ny = r+dxs[3]*i, c+dys[3]*i
        ex, ey = r+dxs[3]*(i-1), c+dys[3]*(i-1)
        arr[nx][ny] = sub[ex][ey]

if d == 0:
    clockwise(r, c, m1, m2, m3, m4)
else:
    clock(r, c, m1, m2, m3, m4)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()