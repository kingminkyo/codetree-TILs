n, m, t = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

count = [
    [ 0 for _ in range(n)]
    for _ in range(n)
]

temp_count = [
    [ 0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x, y = x-1, y-1
    count[x][y] = 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for _ in range(t):
    for i in range(n):
        for j in range(n):
            max_num = -1
            gx, gy = 0, 0 
            if count[i][j] != 0:

                for dx, dy in zip(dxs, dys):
                    nx, ny = i+dx, j+dy
                    if in_range(nx, ny) and arr[nx][ny] >= max_num:

                        max_num = arr[nx][ny]
                        gx, gy = nx, ny

                # print(i, j, gx, gy)
                
                temp_count[gx][gy] += 1

    for i in range(n):
        for j in range(n):
            count[i][j] = temp_count[i][j]
            if count[i][j] >= 2:
                count[i][j] = 0
            temp_count[i][j] = 0

    # for i in range(n):
    #     for j in range(n):
    #         print(count[i][j], end=" ")
    #     print()

cnt = 0 

for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            cnt+= 1 

print(cnt)