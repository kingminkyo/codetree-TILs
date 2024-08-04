n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

demo = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 0 
bomb_bsk = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1
            bomb_bsk.append((i, j))

ans = []

def print_ans():
    for a in ans:
        print(a, end="")
    print()

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def reset_demo():
    for i in range(n):
        for j in range(n):
            demo[i][j] = 0
def print_demo():
    for i in range(n):
        for j in range(n):
            print(demo[i][j], end=" ")
        print()
    print()

def select():
    reset_demo()
    count = 0 
    for i in range(len(bomb_bsk)):
        x, y = bomb_bsk[i]
        num = ans[i]
        count = bomb(x, y, num)
    # print_demo()
    # print(count)
    return count 

def bomb(x, y, num):
    if num == 1:
        dxs, dys = [0, 1, 2, -1, -2], [0, 0, 0, 0, 0]
    elif num == 2:
        dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
    else: 
        dxs, dys = [0, -1, -1, 1, 1], [0, 1, -1, 1, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            demo[nx][ny] = 1

    count = 0
    for i in range(n):
        for j in range(n):
            if demo[i][j] == 1:
                count += 1

    return count

    



result = 0
def choose(num):
    global result

    if num == cnt:
        # print_ans()
        result = max(result, select())
        return
    
    for i in range(1, 4):
        ans.append(i)
        choose(num+1)
        ans.pop()

choose(0)

print(result )