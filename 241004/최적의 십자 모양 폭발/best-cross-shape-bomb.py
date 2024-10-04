n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

copy_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def copy():
    for i in range(n):
        for j in range(n):
            copy_arr[i][j] = arr[i][j]

# 3
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def print_arr():
    for i in range(n):
        for j in range(n):
            print(copy_arr[i][j], end=" ")
        print()
    print()

def bomb(x, y):
    copy()

    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
    num = arr[x][y]

    for dx, dy in zip(dxs, dys):
        for i in range(num):
            nx, ny = x+dx*i, y+dy*i
            
            # print(num, x, y, nx, ny)

            if in_range(nx, ny):
                # print("true")
                copy_arr[nx][ny] = 0
            
    # print_arr()
    
def drop():

    for j in range(n):
        temp = []
        for i in range(n-1, -1, -1):
            if copy_arr[i][j] != 0:
                temp.append(copy_arr[i][j])

        for i in range(n):
            copy_arr[i][j] = 0

        num = n-1 
        for t in temp:
            copy_arr[num][j] = t
            num -= 1 

    # print_arr()



def check_twin():
    cnt = 0 

    dxs, dys = [1, 0], [0, 1]

    # print("트윈")
    for i in range(n):
        for j in range(n):
            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy

                if in_range(nx, ny) and copy_arr[i][j] == copy_arr[nx][ny]:
                    if copy_arr[i][j] != 0:
                        cnt += 1 
                    
                    # print(i, j, nx, ny)
                    
    # print(cnt, "next")
    return cnt 

result = 0 

for i in range(n):
    for j in range(n):
        bomb(i, j)
        drop()
        result = max(check_twin(), result)


print(result)