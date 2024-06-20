direct = input()

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

c_dir = 3

for d in direct:

    if d == "F":
        x += dx[c_dir]
        y += dy[c_dir]

    if d == "L":
        c_dir = (c_dir - 1 + 4) % 4
    if d == "R":
        c_dir = (c_dir + 1) % 4

    


    
print(f"{x} {y}")