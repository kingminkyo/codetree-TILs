n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

bomb_arr =[
    int(input())
    for _ in range(m)
]
def p_print():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

def bomb(x, y, k):
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

    for i in range(k):
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx*i, y+dy*i

            if in_range(nx, ny):
                arr[nx][ny] = 0
    # p_print()



def rain():

    for i in range(n):
        temp = [0 for _ in range(n)]
        idx = 0

        for j in range(n-1, -1, -1):
            if arr[j][i] != 0:
                temp[idx] = arr[j][i]
                idx += 1
        
        for j in range(n-1, -1, -1):
            arr[j][i] = temp[n-1-j]
    # p_print()

for c in bomb_arr:
    
    c -= 1
    r = 0
    num = 0
    for i in range(n):
        if arr[i][c] > 0:
            num = arr[i][c]
            r = i
            break
    
    bomb(r, c, num)
    rain()




            

p_print()