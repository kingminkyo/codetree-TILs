n = int(input())
arr = [
    input()
    for _ in range(n)
]
player = [
    input()
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, 1, -1, 1, -1]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for i in range(n):
    for j in range(n):
        if player[i][j] == "x":
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy
                if in_range(nx, ny) and arr[nx][ny] == "*":
                    cnt += 1
            print(cnt, end="")
        else:
            print(".", end="")
            continue
    print()