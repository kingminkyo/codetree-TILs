n, m, q = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def print_arr():
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print()
def rotate(x1, y1, x2, y2):
    
    temp1 = arr[x2][y1]
    temp2 = arr[x2][y2]
    temp3 = arr[x2][y1]

    for i in range(y2, y1, -1):
        arr[x1][i] = arr[x1][i-1]
    
    for i in range(x2, x1, -1):
        arr[i][y2] = arr[i-1][y2]
    
    
    for i in range(y1, y2):
        arr[x2][i] = arr[x2][i+1]

    for i in range(x1, x2):
        arr[i][y1] = arr[i+1][y1]

    arr[x1+1][y2] = temp1
    arr[x2][y2-1] = temp2
    arr[x1+1][y1] = temp3

copy = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def do_copy():
    for i in range(n):
        for j in range(m):
            copy[i][j] = arr[i][j]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

def comp_switch(x, y):
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    cnt = 1
    num = copy[x][y]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            cnt += 1
            num += copy[nx][ny]
        # print(nx, ny)
    
    # print(num, cnt, "흐압")
    arr[x][y] = int(num/cnt)


for _ in range(q):
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1 

    rotate(r1, c1, r2, c2)
    # print_arr()
    # print(copy)
    do_copy()

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            comp_switch(i, j)

    print_arr()