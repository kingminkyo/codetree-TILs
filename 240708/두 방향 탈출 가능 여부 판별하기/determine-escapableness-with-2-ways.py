n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y):

    if not in_range(x, y):
        return False

    if visited[x][y] ==1 or arr[x][y] == 0:
        
        return False
    
    return True

def dfs(x, y):

    dxs, dys = [1, 0], [0, 1]

    # print("already", x, y)

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        # print(x, y, nx, ny, dx, dy)
        if can_go(nx, ny):
            # print("can")
            visited[nx][ny] = 1
            dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)
# for i in range(n):
#     for j in range(m):
#         print(visited[i][j], end=" ")
#     print()

if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)