from collections import deque

# 입력 받기
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방문 시간을 기록할 배열
visited = [[-1 for _ in range(n)] for _ in range(n)]

# 방향 벡터 (우, 하, 좌, 상)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 큐 초기화
q = deque()

# 초기 상한 귤의 위치를 큐에 추가
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            q.append((i, j))
            visited[i][j] = 0

# BFS 수행
while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

# 출력 준비
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            visited[i][j] = -1
        elif arr[i][j] == 1 and visited[i][j] == -1:
            visited[i][j] = -2

# 출력
for row in visited:
    print(" ".join(map(str, row)))