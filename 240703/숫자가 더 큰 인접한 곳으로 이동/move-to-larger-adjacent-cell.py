n, r, c = tuple(map(int, input().split()))

x, y = r-1, c-1 
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

print(arr[x][y], end=" ")

while True:
    
    new_x, new_y = x, y 
    can_go = False

    for dx, dy in zip(dxs, dys):

        nx, ny = x+dx, y+dy

        # print(nx, ny)

        if not in_range(nx, ny):
            continue
        
        if arr[nx][ny] > arr[x][y]:
            new_x, new_y = nx, ny
            can_go = True
            break

    x = new_x
    y = new_y


    if not can_go:
        break

    print(arr[x][y], end=" ")