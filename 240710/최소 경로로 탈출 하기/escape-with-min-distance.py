n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for i in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

from collections import deque

q = deque()

def push(x, y, num):
    visited[x][y] = num
    q.append((x, y))

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if can_go(nx, ny):
                push(nx, ny, visited[x][y] + 1)

push(0, 0, 0)
bfs()

if visited[n-1][m-1]:
    print(visited[n-1][m-1])
else:
    print(-1)