n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n


# 1 2 3 4 
dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]


def rolling(x, y, k, l):
    result = 0

    roll = [k, l, k, l] # 2 3 2 3 
    
    current = 0
    for dx, dy, z in zip(dxs, dys, roll):
        for _ in range(z):
            
            x, y = x + dx, y+dy

            if not in_range(x, y):
                return 0
            
            current += arr[x][y]

        
        
    return current

hap = 0 

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                curr = rolling(i, j, k, l)      
                hap = max(curr, hap)


print(hap)