n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and  x<n and y>=0 and y<m


# def can_include(x, y):

result = 0 

dxs = [1, 1, -1, -1]
dys = [1, -1, -1, 1]

for x in range(n):
    for y in range(m):
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if in_range(nx, ny):
                comp = grid[x][y] + grid[nx][y] + grid[x][ny]
                # print(f"{x} {y} {nx} {ny} {grid[x][y]} {grid[nx][y]} {grid[x][ny]}")
                result = max(result, comp)
            
dxs = [2, -2, 0, 0]
dys = [0, 0, 2, -2]

for x in range(n):
    for y in range(m):
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                comp = grid[x][y] + grid[nx][y] + grid[x][ny]
                result = max(result, comp)

print(result)