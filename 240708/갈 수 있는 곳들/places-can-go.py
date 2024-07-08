from collections import deque

n, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 1:
        return False
    return True

q = deque()

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1
                

start_point = []

for _ in range(k):
    a, b = map(int, input().split())
    a, b = a-1, b-1

    start_point.append((a, b))

for x, y in start_point:
    q.append((x, y))
    visited[x][y] = 1
    bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1 
print(cnt)