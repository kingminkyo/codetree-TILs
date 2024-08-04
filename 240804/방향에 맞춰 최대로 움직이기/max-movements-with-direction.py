n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

d_dir = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 


ans = 0 
def find_path(x, y, cnt):
    global ans 
    
    ans = max(cnt, ans)
    
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    d = d_dir[x][y] -1

    for i in range(1, n) :
        nx, ny = x + dxs[d] * i, y + dys[d] * i

        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            print(arr[nx][ny])
            # find_path(nx, ny, cnt+1)
r, c = tuple(map(int, input().split()))

find_path(r-1, c-1, 0)

print(ans)