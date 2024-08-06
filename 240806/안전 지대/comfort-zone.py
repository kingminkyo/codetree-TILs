n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def reset_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 :
        return False
    return True

count = 0 
def dfs(x, y, k):
    
    dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        
        if can_go(nx, ny, k):
            visited[nx][ny] = 1
            dfs(nx, ny, k)

max_num = 0
def print_visited():
    for i in range(n):
        for j in range(m):
            print(visited[i][j], end=" ")
        print()
    print()
        
for i in range(n):
    for j in range(m):
        max_num = max(max_num, arr[i][j])
# print(max_num)

result = 0
result_k = 1
for k in range(1, max_num+1):
    count = 0
    reset_visited()

    for i in range(n):
        for j in range(m):
            if arr[i][j] <= k:
                visited[i][j] = 1


    # print_visited()

    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                dfs(i, j, k)
                count += 1 

    # print("k는 ", k, "zone은 ", count , result)
    # print_visited()
    
    if count > result:
        result = count
        result_k = k

print(result_k, result )