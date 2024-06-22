n, m = tuple(map(int, input().split())) # 1 , 6 

arr =[
    [0] * m
    for _ in range(n)
]

arr[0][0] = 1

dx, dy =  [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return x>=0 and x<m and y>=0 and y<n

cnt = 0
x, y = 0, 0
dn = 0
for i in range(2, m*n +1):
    nx, ny = x+dx[dn], y+dy[dn]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dn = (dn + 1) % 4

    x, y = x+dx[dn], y+dy[dn]
    
    arr[x][y]=i


for i in range(n):
    for j in range(m):
        print(f"{arr[i][j]}", end=" ")
    print()