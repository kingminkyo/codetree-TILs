n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [ 0 for _ in range(m)]
    for _ in range(n)
]


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 1:
        return False
    return True

from collections import deque
q = deque()

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs():

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                visited[nx][ny] += 1
                q.append((nx, ny))

def ice(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if in_range(nx, ny) and arr[nx][ny] == 1:
            arr[nx][ny] = 0
    
def print_visited():
    for i in range(n):
        for j in range(m):
            print(visited[i][j], end=" ")
        print()
    print()

def print_arr():
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print()

on = False
cnt = 0 
memory_cnt = 0
curr_time = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1 
memory_cnt = cnt 

def reset_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0


for time in range(1, 1000):

    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and visited[i][j] == 0 and not on:
                q.append((i, j))
                visited[i][j] += 1
                bfs()
                on = True

            
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                ice(i, j)
            
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1 

    if cnt == 0:
        curr_time = time
        break

    memory_cnt = cnt 
    
    reset_visited()
    # print_visited()
    # print_arr()
    on = False

print(curr_time, memory_cnt)