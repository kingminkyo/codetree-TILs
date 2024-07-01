n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())
r, c = r-1, c-1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def bomb(x, y):
    num = arr[x][y]
    arr[x][y] = 0

    for i in range(1, num):
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx*i, y+dy*i

            if in_range(nx, ny):
                arr[nx][ny] = 0


def clear():
    
    for i in range(n):
        temp = [0 for _ in range(n)]
        index = 0
        # print(temp)

        for j in range(n-1, -1, -1):
            if arr[j][i] != 0:
                temp[index] = arr[j][i]
                index += 1
        
        for j in range(n-1, -1, -1):
            arr[j][i] = temp[n-1-j]
        











bomb(r, c)
clear()





for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()