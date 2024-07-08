# import sys
# sys.setrecursionlimit(250000)

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y ):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y, num):
    if not in_range(x, y):
        return False
    
    if not visited[x][y] and arr[x][y] == num:
        return True
    return False

block_cnt = 0
block_size = 0
block = 0

def dfs(x, y):
    global block
    
    num = arr[x][y]

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if can_go(nx, ny, num):
            block += 1 
            visited[nx][ny] = 1 
            dfs(nx, ny)



for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block = 0
            # visited[i][j] = 1 
            dfs(i, j)

            if block >= 4:
                block_cnt += 1 
            block_size = max(block_size, block)
        
print(block_cnt, block_size)