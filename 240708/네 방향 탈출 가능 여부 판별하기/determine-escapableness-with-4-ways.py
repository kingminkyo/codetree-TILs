from collections import deque
q = deque()


n, m = map(int, input().split())

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
    if visited[x][y] == 1 or arr[x][y] == 0:
        return False
    return True

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))
                
visited[0][0] = 1
q.append((0, 0))
bfs()
# print(n, m)
# print(visited)
if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)