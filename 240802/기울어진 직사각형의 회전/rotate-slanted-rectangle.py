n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c, k, l, k, l, to = tuple(map(int, input().split()))

# to가 0 반시계
# to가 1 시계방향 

save = []

dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]

def clockwise(r, c):
    t_dir = [k, l, k, l]
    cnt = 0
    x, y = r-1, c-1 

    temp = arr[x][y]

    for dx, dy in zip(dxs, dys):
        for _ in range(t_dir[cnt]):
            x, y = x+dx, y+dy
            swap = arr[x][y]
            arr[x][y] = temp
            temp = swap 

        cnt += 1

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()

clockwise(r, c)
print_arr()