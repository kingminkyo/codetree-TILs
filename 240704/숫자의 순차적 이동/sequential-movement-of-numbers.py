n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n


def swap(x, y):
    num = -1
    cx, cy = x, y
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and arr[nx][ny] > num:
            cx, cy = nx, ny
            num = arr[nx][ny]
    
    arr[x][y], arr[cx][cy] = arr[cx][cy], arr[x][y]
            

for _ in range(m):
    for num in range(1, n*n+1):

        ok = False
        for i in range (n):
            for j in range(n):
                if arr[i][j] == num:
                    swap(i, j)
                    ok = True
                    break
            if ok:
                break
        # print(num)
        # for i in range(n):
        #     for j in range(n):
        #         print(arr[i][j], end=" ")
        #     print()
        # print()

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()