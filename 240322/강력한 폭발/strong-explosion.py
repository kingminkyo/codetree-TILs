n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

area = grid
print(area)
spare_area = grid 

# 폭탄의 개수를 센다
# 폭탄마다 각각 1, 2, 3번 폭탄을 시행한다
# 폭탄 시행 시마다 터진 지역을 계산하고, 누적한다
# 다른 폭탄 시행 시 area를 초기화한다

bomb_num = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_num += 1 
print(bomb_num)
# 격자이므로 
def in_range(x, y):
    return x>=0 and  x<n and y>=0 and y<n 

def bomb(x, y, num):
    if num == 1:
        dxs, dys =  [1, 2, -1, -2] , [0, 0, 0, 0] 
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                area[nx][ny] = 1

    if num == 2:
        dxs, dys = [1, 0, -1, 0] , [0, -1, 0, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                area[nx][ny] = 1

    if num == 3:
            dxs, dys = [1, 1, -1, -1] , [1, -1, -1, 1]
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny):
                    area[nx][ny] = 1

result_num = 0

def count_bad():
    global area
    global grid
    global result_num
    bad = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] == 1:
                bad += 1 

    for i in range(n):
        print(area[i])
    print()
    area = grid
    result_num -= 1
    return bad




def start(x, y):
    global result_num
    global bomb_num

    if result_num == bomb_num:

        print(count_bad())
        return

    for i in range(x, n):
        for j in range(y, n):
            if grid[i][j] == 1:
                for k in range(1, 4):
                    result_num += 1
                    bomb(i, j, k)
                    start(i, j)


start(0, 0)