n, k = tuple(map(int, input().split()))
import sys

sys.setrecursionlimit(10000)




arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

def can_go(x, y, num):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == 1 or arr[x][y] >= num:
        return False
    return True

max_num = 0

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    global max_num
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if can_go(nx, ny, max_num):
                # print("메모리 시점", nx, ny)
                q.append((nx, ny))
                visited[nx][ny] = 1
                
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

from collections import deque
q = deque()

check = 0 


r, c = tuple(map(int, input().split()))
r, c = r-1, c-1 
visited[r][c] = 1
q.append((r, c))
max_num = arr[r][c]
nr, nc = 0, 0
for _ in range(k):
    # print(r, c )
    bfs()
    check = 0
    for i in range(n):
        for j in range(n):
            if i == r and j == c:
                continue
            if visited[i][j] and arr[i][j] > check:
                check = arr[i][j]
                # print(check, i, j)
                nr, nc = i, j
    # print(nr, nc)
    # print_visited()
    reset_visited()

    r, c = nr, nc
    visited[r][c] = 1
    q.append((r, c))
    max_num = arr[r][c]
    
    

print(r+1, c+1)