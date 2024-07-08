n = int(input())

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
def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] == 1 or arr[x][y] == 0:
        return False
    return True


cnt = 0 
def dfs(x, y):
    global cnt 

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny):
            cnt += 1 
            visited[nx][ny] = 1
            dfs(nx, ny)

ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(i, j)

        if cnt >= 1:
            ans.append(cnt)
        cnt = 0

print(len(ans))
ans.sort()
for a in ans:
    print(a)