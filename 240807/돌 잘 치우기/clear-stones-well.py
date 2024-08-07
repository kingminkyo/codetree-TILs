n, k, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

starts = []
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    x, y = x-1, y-1 

    starts.append((x, y))

rocks = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            rocks.append((i, j))

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

copy = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def copy_arr():
    for i in range(n):
        for j in range(n):
            copy[i][j] = arr[i][j]


ans = []

from collections import deque
q = deque()


def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or copy[x][y] == 1:
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


def count_place():
    for start in starts:
        x, y = start
        if can_go(x, y):
            visited[x][y] = 1
            q.append((x, y))

def print_visited():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()

def clear_rocks_and_bfs():
    reset_visited()
    copy_arr()

    for a in ans:
        x, y = rocks[a]
        copy[x][y] = 0

    for start in starts:
        x, y = start
        if can_go(x, y):
            visited[x][y] = 1
            q.append((x, y))
            bfs()

    # print_visited()
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                count += 1 
    
    return count

    
    

result = 0

def choose(num, cnt):
    global result
    if cnt == m:
        
        result = max(result, clear_rocks_and_bfs())

        # print(result)
        return
    if num == len(rocks):
        return

    ans.append(num)
    choose(num+1, cnt+1)
    ans.pop()

    choose(num+1, cnt)


choose(0, 0)
print(result)