n = int(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)
    
    if c_dir == "E":
        x += dist * dx[0]
        y += dist * dy[0]

    if c_dir == "S":
        x += dist * dx[1]
        y += dist * dy[1]

    if c_dir == "W":
        x += dist * dx[2]
        y += dist * dy[2]

    if c_dir == "N":
        x += dist * dx[3]
        y += dist * dy[3]
    
print(f"{x} {y}")