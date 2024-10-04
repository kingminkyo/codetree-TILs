n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]



def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

# 1번 / 
# 2번 \ 



def start(x, y, d_dir):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]   
    time = 1

    nx, ny = x+dx[d_dir], y+dy[d_dir]
    # print(nx, ny, d_dir)

    while(in_range(nx, ny)):
        time += 1

        if arr[nx][ny] == 1:
            if d_dir == 1 or d_dir == 3:
                d_dir += 1
            else:
                d_dir -= 1
        elif arr[nx][ny] == 2:
            if d_dir == 2 or d_dir == 0:
                d_dir += 1
            else:
                d_dir -= 1
            
        d_dir = (d_dir + 4) % 4 

        nx, ny = nx+dx[d_dir], ny+dy[d_dir]
        
        # print(nx, ny, d_dir, time)
    
    
    return time

result = 0 

for i in range(n):
    result = max(result, start(i, -1, 0))

for i in range(n):
    result = max(result, start(-1, i, 1))

for i in range(n):
    result = max(result, start(i, n, 2))

for i in range(n):
    result = max(result, start(n, i, 3))

print(result)