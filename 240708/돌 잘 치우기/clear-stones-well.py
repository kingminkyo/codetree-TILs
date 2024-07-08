n, k, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

start_num = []
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    x, y = x-1, y-1
    start_num.append((x, y))

# print(start_num)
#백트래킹 #bfs 

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or copy[x][y] == 1:
        return False
    return True

from collections import deque

q = deque()

check = 0
count = 0

def bfs():
    global check
    global count 

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                count += 1
                visited[nx][ny] = 1
                q.append((nx, ny))


ans = []

def print_ans():
    for a in ans:
        print(a, end=" ")
    print()
    
cnt_rock = 0
loc_rock = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            loc_rock.append((i, j))
            cnt_rock += 1 

copy = [
    [0 for _ in range(n)]
    for _ in range(n)
]
def copy_arr():
    for i in range(n):
        for j in range(n):
            copy[i][j] = arr[i][j]

def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def print_visited():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()

check = 0
count = 0
# print (loc_rock)
def choose(curr_num, cnt):
    global count
    global check
    if curr_num == cnt_rock:
        if cnt == m:
            count = 0
            copy_arr()
            reset_visited()
            # print(arr)
            for a in ans:
                new_x, new_y = loc_rock[a]
                copy[new_x][new_y] = 0

            for nx, ny in start_num:
                count = 1
                visited[nx][ny] = 1
                q.append((nx, ny))
                bfs()
                # print("x, y : ", nx, ny, "count, check:", count,check)
    
                check = max(check, count)
            

            # check = max(check, count)

            # print_visited()
            # print_ans()
        return

    ans.append(curr_num)
    choose(curr_num+1, cnt+1)
    ans.pop()

    choose(curr_num+1, cnt)

choose(0, 0)
print(check)