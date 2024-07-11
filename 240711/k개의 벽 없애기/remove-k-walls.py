n, k = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


r1, c1 = tuple(map(int, input().split()))
r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

walls = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            walls.append((i, j))

copy = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def arr_copy():
    for i in range(n):
        for j in range(n):
            copy[i][j] = arr[i][j]
            visited[i][j] = 0

ans = []
def remove_walls():
    # print(walls)
    for a in ans:
        x, y = walls[a]
        copy[x][y] = 0


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or copy[x][y] != 0:
        return False
    return True

from collections import deque
q = deque()

def push(x, y, num):
    visited[x][y] = num
    q.append((x, y))
    # print_visited()
    

def print_visited():
    for i in range(n):
        for j in range(n):
            print(copy[i][j], end=" ")
        print()
    print()

    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    # print("go")
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny, visited[x][y]+1)


def print_ans():
    for a in ans:
        print(a, end=" ")
    print()


def check():
    arr_copy()
    remove_walls()
    global r1
    global c1
    global r2
    global c2
    
    push(r1, c1, 1)
    bfs()
    # print_visited()
    if not visited[r2][c2]:
        return 10000
    else:
        return visited[r2][c2]


min_time = 10000
def choose(curr_num, cnt):
    global min_time
    # global r1
    # global c1
    # global r2
    # global c2 

    if curr_num == len(walls):
        if cnt == k:
            # print_ans()
            
            # print(copy)
            # print(check())
            min_time = min(check(), min_time)
            
            bfs()


        return

    ans.append(curr_num)
    choose(curr_num+1, cnt+1)
    ans.pop()

    choose(curr_num+1, cnt)

choose(0,0)

if min_time==10000:
    print(-1)
else:
    print(min_time-1)