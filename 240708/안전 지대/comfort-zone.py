import sys

sys.setrecursionlimit(10**5)

n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x,y, k):
    if not in_range(x, y):
        return False

    if visited[x][y] or arr[x][y] <= k :
        return False
    return True

max_k = 0

for i in range(n):
    for j in range(m):
        max_k = max(max_k, arr[i][j])

def dfs(x, y, k):

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if can_go(nx, ny, k):

            visited[nx][ny] = 1
            dfs(nx, ny, k)

def reset_all():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0


cnt = 0
result_k = 1
result_a = 0
for k in range(1, max_k+1):
    cnt = 0
    reset_all()
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = 1
                cnt += 1 
                dfs(i, j, k)
    # print(k)
    # for i in range(n):
    #     for j in range(m):
    #         print(visited[i][j], end=" ")
            
    #     print()
    # print(cnt)
    # print()

    if result_a < cnt:
        result_a = cnt
        result_k = k


print(result_k, result_a)