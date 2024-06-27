n = int(input())
arr =[
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1] 


def in_range(x, y):
    return x>=0 and x< n and y>=0 and y<n

def square(x, y, k, l):
    nx, ny = x, y 
    result = 0
    
    move_nums = [k, l, k, l]

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x+dx, y+dy

            if not in_range(x, y):
                return 0
        
            result += arr[x][y]
        
    return result


ans = 0

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, square(i, j, k, l))


    
print(ans)