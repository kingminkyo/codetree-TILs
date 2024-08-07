n, k, u, d = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

arr_num = []

for i in range(n):
    for j in range(n):
        arr_num.append((i, j))



def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x1, y1, x2, y2):


    if not in_range(x2, y2):
        return False
    diff = abs(arr[x1][y1] - arr[x2][y2])

    if visited[x2][y2] == 1 or not (diff >= u and diff <= d):
        return False
    return True

from collections import deque
q = deque()

def print_visited():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=" ")
        print()

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(x, y, nx, ny):
                # print(x, y, nx, ny)
                visited[nx][ny] = 1
                q.append((nx, ny))

        # print_visited()

ans = []

def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0


result = 0 
def collect_and_bfs():
    start_points = []
    reset_visited()

    for point in ans:
        start_points.append(arr_num[point])
    
    # print(start_points)
    
    # 그러면 0,0과 0,1이 저장 됨 
    for point in start_points:
        x, y = point 
        visited[x][y] = 1
        q.append((x, y))
        bfs()

    count = 0 

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                count+=1 

    return count

def choose(num, cnt):
    global result
    if cnt == k:
        # print(ans)
        result = max(result, collect_and_bfs())
        return

    if num == (n*n):
        return
    
    ans.append(num)
    choose(num+1, cnt+1)
    ans.pop()

    choose(num+1, cnt)

choose(0, 0)
print(result)