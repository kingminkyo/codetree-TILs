n, m, x, y = tuple(map(int, input().split()))
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]
x, y = x-1, y-1 

def copy():
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

arr[x][y] = 1

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def p_print():
    for i in range(n):
        for j in range(n):
            print(temp[i][j], end=" ")
        print()
    print()

def spread_bomb(x, y, t):
    k = 2 ** (t-1)
    k = int(k)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx*k, y + dy*k
        if in_range(nx, ny):
            temp[nx][ny] = 1
    
    
    

    



for t in range(m+1):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                spread_bomb(i, j, t)
                p_print()

    copy()

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] >= 1:
            cnt += 1
print(cnt)