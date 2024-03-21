n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = tuple(map(int, input().split()))

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y, comp):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] >=comp :
        return False
    return True

from collections import deque

q = deque()
comp = grid[r-1][c-1]
def bfs():

    dxs, dys = [1, 0, -1, 0] , [0, -1, 0, 1]
    global comp
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            
            nx, ny = x+dx, y+dy

            if can_go(nx, ny, comp):
                visited[nx][ny] = True
                q.append((nx, ny))


def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


# q.append((3, 2))
# bfs()


for i in range(k):
    comp = grid[r-1][c-1]
    q.append((r-1, c-1))
    bfs()
    
    rull = 0
    for j in range(n):
        for k in range(n):
            if grid[j][k] > rull and visited[j][k]:
                rull = grid[j][k]
                r, c = j+1, k+1
    # for i in range(n):
    #     print(visited[i])
    
    # print(f"{r} {c}")
    reset_visited()


print(f"{r} {c}")