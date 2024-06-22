n, t = tuple(map(int, input().split()))
x, y, d = tuple(input().split())
x, y = int(x), int(y)

x -= 1
y -= 1 

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
mapper = {
    "R":0,
    "D":1,
    "L":2,
    "U":3
}

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

move_dir = mapper[d]

for i in range(t):
    if in_range(x+dx[move_dir], y+dy[move_dir]):
        x, y = x+dx[move_dir], y+dy[move_dir]
    
    else:
        move_dir = (move_dir + 2) % 4

    
print(f"{x+1} {y+1}")