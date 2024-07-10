n, h, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)   
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 1:
        return False
    return True
from collections import deque

q = deque()
def push(x, y, num):
    q.append((x, y))
    visited[x][y] =num

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny, visited[x][y]+1)


def check_min_dist():
    dist = 20000
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3 and visited[i][j]:
                dist = min(dist, visited[i][j])

    if dist == 20000:
        return -1
    else:
        return dist

def print_visited():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            reset_visited()
            push(i, j, 0)
            bfs()
            step[i][j] = check_min_dist()
            # print_visited()




for i in range(n):
    for j in range(n):
        print(step[i][j], end=" ")
    print()