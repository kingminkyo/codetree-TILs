n, k, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

store_grid = grid

start_arr = [
    list(map(int, input().split()))
    for _ in range(k)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
# m = 치워야 할 돌 개수
# 완전탐색으로 돌 m 개씩 지우고 bfs 진행
# 이동 가능 길이 max가 되는 점 추출 

def in_range(x, y):
    return x>=0, x<n, y>=0, y<n

def can_go(x, y):
    if not in_range:
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

from collections import deque
q = deque()

count = 0

def bfs():
    global count 
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                count+=1
                visited[nx][ny] = True
                q.append((nx, ny))

def reset_visit_and_grid():
    global grid
    global store_grid
    grid = store_grid

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

q.append((0, 0))
bfs()

print(count)

#돌을 두개 치우게 되는 모든 경우의 수에
# 시작점을 기준으로 BFS를 돌린다


    








for i in range(n):
    print(visited[i])