n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n



def rolling(i, j, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]

    route = [k, l, k, l] # 4 2 4 2 로 가정 

    x, y = i, j

    num = 0
    cnt = 0
    for dx, dy in zip(dxs, dys):
         
        for _ in range(route[cnt]):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                x, y = nx, ny
                num += arr[x][y]
                
            else:
                return 0 
        cnt += 1
    # print()
    return num 

result = 0

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                
                hap = rolling(i, j, k, l)
                if hap > result:
                    # print(i, j, k, l)
                    result = hap


print(result )