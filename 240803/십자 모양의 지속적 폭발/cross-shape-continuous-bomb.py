n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()
# 열 선택
def select(num):
    col = num-1 

    for i in range(n):
        if arr[i][col] != 0:
            bomb(i, col)
            return
    return

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

# 폭발 
def bomb(x, y):
    cnt = arr[x][y] - 1
    arr[x][y] = 0
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    
    # print(cnt)
    for dx, dy in zip(dxs, dys):
        nx, ny = x, y 
        
        for _ in range(cnt):
            nx, ny = nx+dx, ny+dy 
            if in_range(nx, ny):
                arr[nx][ny] = 0
                # print(nx, ny)
            else:
                break

# 정렬 

def arrange():
    for i in range(n):
        temp = [ 0 for _ in range(n)]
        cnt = 0

        for j in range(n-1, -1, -1):
            if arr[j][i] != 0:
                temp[cnt] = arr[j][i]
                cnt += 1
        cnt = 0
        for j in range(n-1, -1, -1):
            arr[j][i] = temp[cnt]
            cnt += 1 

for _ in range(m):
    num = int(input())
    select(num)
    arrange()
    print_arr()