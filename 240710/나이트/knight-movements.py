n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1 
visited = [
    [0 for i in range(n)]
    for _ in range(n)
]
step = [
    [-1 for i in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True
    

from collections import deque
q = deque()

def push(x, y, num):
    visited[x][y] = num
    step[x][y] = num
    q.append((x, y))
def bfs():

    dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny, visited[x][y] + 1)


push(r1, c1, 0)
bfs()
# print(step)
if step[r2][c2] != 0:
    print( step[r2][c2])
else:
    print(-1)