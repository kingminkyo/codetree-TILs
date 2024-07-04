n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

bomb_num = 0
bomb_area = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bomb_num += 1 
            bomb_area.append((i, j))

def in_range(x, y ):
    return x>=0 and x<n and y>=0 and y<n

def bomb1(x, y):
    dxs, dys = [0, 1, 2, -1, -2], [0, 0, 0, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            temp[nx][ny] = 1

    
def bomb2(x, y):
    dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            temp[nx][ny] = 1
def bomb3(x, y):

    dxs, dys = [0, -1, -1, 1, 1], [0, 1, -1, 1, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            temp[nx][ny] = 1

def bomb(num, x, y):
    if num == 1:
        bomb1(x, y)
    elif num == 2:
        bomb2(x, y)
    elif num == 3:
        bomb3(x, y)

def clear_temp():
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0


ans = []

def print_ans():
    for a in ans:
        print(a, end="")
    print()

check_cnt = 0

def check_count():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] >= 1:
                cnt += 1
    return cnt 

def print_temp():
    for i in range(n):
        for j in range(n):
            print(temp[i][j], end=" ")
        print()
def choose(curr_num):
    global check_cnt
    if curr_num == bomb_num:
        # print_ans()
        for index, num in enumerate(ans):
            x, y = bomb_area[index]
            bomb(num, x, y)
        check_cnt = max(check_cnt, check_count())
        # print_temp()
        clear_temp()

        return
    
    for i in range(1, 4):
        ans.append(i)
        choose(curr_num+1)
        ans.pop()

choose(0)
print(check_cnt)