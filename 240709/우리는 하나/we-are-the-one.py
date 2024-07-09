n, k, u, d = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

ans = []

def print_ans():
    # print("ans 현황: ", end=" ")
    for a in ans:
        print(a, end=" ")
    print()
    
from collections import deque
q = deque()

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y, num):
    if not in_range(x, y):
        return False
    if visited[x][y] or not (abs(arr[x][y]-num) >= u and (abs(arr[x][y]-num) <= d)):
        return False
    return True

final = 0
count = 0 


def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    global count
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            # print("차이 계산해보자",nx, ny, arr[x][y])
            if can_go(nx, ny, arr[x][y]):
                visited[nx][ny] = 1
                q.append((nx, ny))
                count += 1 
                # print_visited()
                # print(count, nx, ny)

def print_visited():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()
    print()

def city_check():
    global count 
    count = 0
    reset_visited()
    grid_num = 0
    for i in range(n):
        for j in range(n):
            for a in ans:
                if grid_num == a:
                    visited[i][j] = 1
                    q.append((i, j))
                    count += 1
                    bfs()
                    # print_visited()
            grid_num += 1

    return count 



def choose(curr_num, cnt):
    global final
    global count
    if curr_num == n*n:
        if cnt == k:

            # print_ans()
            final = max(final, city_check())
            # print("final: ",final)
        return

    ans.append(curr_num)    
    choose(curr_num+1, cnt+1)
    ans.pop()

    choose(curr_num+1, cnt)




    
choose(0, 0)

print(final)