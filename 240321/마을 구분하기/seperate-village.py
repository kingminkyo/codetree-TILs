n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n) ]
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if arr[x][y] == 0 or visited[x][y]:
        return False

    return True

count = 0
def dfs(x, y):
    dxs, dys = [0, 0, -1, 1] , [1, -1, 0, 0]
    global count
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            count += 1 
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

result = []
comp = 0
for i in range(n):
    for j in range(n):

        if can_go(i, j):
            count= 0
            visited[i][j] = 1
            dfs(i, j)
            if comp is not count:
                result.append(count)
                count = 0
            
# for i in range(n):
#     for j in range(n):
#         if can_go(i, j):
#             visited[i][j] = 1
#             count = 1

#             dfs(i, j)
#             result.append(count)
# for i in range(n):
#     print(visited[i])

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])