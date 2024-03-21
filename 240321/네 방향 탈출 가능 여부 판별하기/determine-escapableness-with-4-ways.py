n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split())) 
    for _ in range(m) 
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

from collections import deque

order = 1
q = deque()

def push(x, y):
    global order
    answer[x][y] = order
    order += 1
    visited[x][y] = 1
    q.append((x, y))

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx , y+dy

            if can_go(new_x, new_y):
                push(new_x, new_y)

        # for i in range(n):
        #     print(visited[i])

        # print()



push(0, 0)
bfs()

if visited[n-1][m-1]==1:
    print("1")
else:
    print("0")