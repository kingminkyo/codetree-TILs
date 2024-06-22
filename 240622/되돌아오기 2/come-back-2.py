word = input()

x, y = 0, 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


d_dir = 3
cnt = 0
for n in word:
    if n == "F":
        x, y = x+dx[d_dir], y+dy[d_dir]
        

    elif n == "L":
        d_dir = (d_dir - 1 + 4 ) % 4
    elif n == "R":
        d_dir = (d_dir + 1) % 4

    cnt += 1 
    
    
    if x == 0 and y == 0:
        break

print(cnt)