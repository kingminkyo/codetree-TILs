n = int(input())
arr =[
    input() for _ in range(n)
]

start = int(input())

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

x, y = 0, 0


if start <= n:
    d_dir = 0
    x, y = 0, (start-1)
elif start <= 2*n:
    d_dir = 1
    x, y = (start-n), (n-1)

elif start <= 3*n:
    d_dir = 2
    x, y = (n-1), (3*n - start)

else:
    d_dir = 3
    x, y = (4*n - start), 0

# print(f"{start}")
# print(f"{x} {y}")

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

cnt = 0
for _ in range(n * n):
    if ((arr[x][y] == "\\" ) and (d_dir == 1 or d_dir == 3 )) or ((arr[x][y] == "/" ) and (d_dir == 0 or d_dir == 2 )) :
        
        d_dir = (d_dir + 1 ) % 4 
        x, y = x+dxs[d_dir], y+dys[d_dir]

        cnt += 1 
        if not in_range(x, y):
            break


    elif  ((arr[x][y] == "\\" ) and (d_dir == 0 or d_dir == 2 )) or ((arr[x][y] == "/" ) and (d_dir == 1 or d_dir == 3 )) :
        
        d_dir = (d_dir - 1 + 4) % 4 
        x, y = x+dxs[d_dir], y+dys[d_dir]
        
        cnt += 1 

        if not in_range(x, y):
            break

    # print(f"{x} {y}")

print(f"{cnt}")