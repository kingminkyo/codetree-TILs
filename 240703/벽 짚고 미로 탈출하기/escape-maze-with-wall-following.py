n = int(input())
x, y = tuple(map(int, input().split()))
x, y = x-1, y-1

d_dir = 0

arr = []
for _ in range(n):
    arr.append(input())


# print(arr)

def in_range(x, y):
    return x>= 0 and x<n and y>=0 and y<n

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

is_out = False
time_cnt = 0
for time in range(1, n*n):
    cnt = 0 # 4가 되면 아웃 
    time_cnt = time
    #  처음에는 기존 방향 전진 가정
    nx, ny = x+dxs[d_dir], y+dys[d_dir]

    # 바라보고 있는 방향 이동 불가능, 방향전환
    if in_range(nx, ny) and arr[nx][ny] == "#":
        d_dir = (d_dir -1 + 4) % 4

    #이동 가능 1 

    nx, ny = x+dxs[d_dir], y+dys[d_dir]
    if not in_range(nx, ny):
        break

    else:
        x, y = nx, ny

    r_dir = (d_dir + 1 + 4) % 4
    rx, ry = x+dxs[r_dir], y+dys[r_dir]


    if arr[rx][ry] == "#":
        continue
    else:
        d_dir = r_dir
        x, y = x+dxs[d_dir], y+dys[d_dir]
        cnt += 1 

    if cnt >= 4:
        is_out = True

if is_out:
    print(-1)
else:
    print(time_cnt)