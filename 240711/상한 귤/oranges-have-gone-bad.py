n, k = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [-1 for _ in range(n)]
    for _ in range(n)
]

def print_visited():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()
     
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y, num):
    if not in_range(x, y):
        return False
    if arr[x][y] == 0 or (visited[x][y] <= num and visited[x][y] != -1):
        return False
    return True

from collections import deque
q = deque()

def push(x, y, num):
    q.append((x, y))
    visited[x][y] = num

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny, visited[x][y]):
                push(nx, ny, visited[x][y] + 1)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            push(i, j, 0)
            bfs()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == -1:
            visited[i][j] = -2
print_visited()