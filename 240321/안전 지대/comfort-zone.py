n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_int = 0
visited = [
            [0 for _ in range(m)]
            for _ in range(n)
        ]

for i in range(n):
    for j in range(m):
        max_int = max(max_int, arr[i][j])

# print(max_int)


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m


def can_go(x, y, comp):
    if not in_range(x, y):
        return False
    
    if arr[x][y] <= comp or visited[x][y]:
        return False
    return True


count = 0
def dfs(x, y, comp):
    global count
    dxs, dys = [1, 0 ,-1, 0] , [0, -1, 0, 1]

    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y, comp):

            count += 1 
            visited[new_x][new_y] = 1
            dfs(new_x, new_y, comp)
            # print(count)
            # for k in range(n):
            #     print(visited[k])   
            
            


    # print()
# result 
num, result_count = 0, 0
for comp in range(1, max_int):
    # print(comp)
    temp = 0
    result = 0
    for i in range(n):
        for j in range(m):
            
            dfs(i, j, comp)

            if temp is not count:
                result += 1
                # print(f"comp: {comp} safe {result}")
            if result_count < result:
                num = comp
                result_count = result

            temp = count
    count = 0
        
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0

print(f"{num} {result_count}")