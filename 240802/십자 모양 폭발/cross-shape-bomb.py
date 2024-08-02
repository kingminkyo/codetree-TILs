n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = tuple(map(int, input().split()))
r, c = r-1, c-1 


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

def bomb(x, y):
    num = arr[x][y]

    arr[x][y] = 0
    if num == 1:
        return 
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        for _ in range(num-1):
            if in_range(nx, ny):
                arr[nx][ny] = 0
                nx, ny = nx+dx, ny+dy
def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()

def arrange():
    
    for i in range(n):
        temp = [ 0 for _ in range(n) ]

        cnt = 0
        for j in range(n-1, -1, -1):
            if arr[j][i] != 0:
                temp[cnt] = arr[j][i]
                cnt += 1 
        cnt = 0
        for j in range(n-1, -1, -1):
            arr[j][i] = temp[cnt]
            cnt += 1


bomb(r, c)
arrange()
print_arr()