n = int(input())

arr = [
    list(map(int, input().split())) for _ in range(n)
]

def in_range(x, y):
    return x < n and x>=0 and y<n and y>=0

dx, dy = [1, 0, -1, 0] , [0, -1, 0, 1]

result = 0 
for i in range(n):
    for j in range(n):
        cnt = 0
        for dxs, dys in zip(dx, dy):
            
            if in_range(i+dxs, j+dys) and arr[i+dxs][j+dys] == 1 :
                cnt += 1 
        if cnt >= 3:
            result += 1 

print(result)