n, k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

diff = [
    list(map(int, input().split()))
    for _ in range(k)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

answer = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False

    return True

from collections import deque

q = deque()
order = 0
def push(x, y):
    global order
    order += 1 
    answer[x][y] = order
    visited[x][y] = True
    q.append((x,y))

count = 1
def bfs():
    dxs, dys = [1, 0, -1, 0] , [0, -1, 0, 1]
    
    global count
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            
            if can_go(new_x, new_y):
                count += 1
                push(new_x, new_y)    


for i in range(k):
    push(diff[i][0], diff[i][1])
    bfs()


print(count)
# for i in range(k):
#     q.append((1,1))
#     bfs()

# for i in range(n):
#     print(visited[i])


# print(count)