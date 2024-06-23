n, t = tuple(map(int, input().split()))

words = input()

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

mid = int(n/2)

x, y = mid, mid

dxs, dys = [0, -1, 0, 1] , [-1, 0, 1, 0]
d_dir = 1

result = arr[x][y]

for w in words:
    if w == "L":
        d_dir = (d_dir - 1 + 4) % 4

    elif w == "R":
        d_dir = (d_dir + 1) % 4 

    elif w == "F":
        nx, ny = x+dxs[d_dir] , y+dys[d_dir]
        if in_range(nx, ny):
            x, y = nx, ny
            result += arr[x][y]


print(result)