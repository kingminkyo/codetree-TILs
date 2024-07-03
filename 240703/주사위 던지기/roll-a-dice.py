n, m, r, c = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
commands =  list(input().split()) 
# print(arr)
dice = {
    "u":1,
    "d":6,
    "f":2,
    "b":5,
    "r":3,
    "l":4
}
x, y = r-1, c-1 

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

d_dir = 0

arr[x][y] = dice["d"]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

for c in commands:
    # U D R L 
    u, d, f, b, r, l = "u", "d", "f", "b", "r", "l"    
    
    ex = dice

    if c == "R":
        d_dir = 0

    if c == "D":
        d_dir = 1
    
    if c == "L":
        d_dir = 2

    if c == "U":
        d_dir = 3
    
    nx, ny = x+dxs[d_dir], y+dys[d_dir]

    if in_range(nx, ny):
        x, y = nx, ny
        if c == "R":
            temp = dice[d]
            dice[d] = dice[r]
            dice[r] = dice[u]
            dice[u] = dice[l]
            dice[l] = temp
            d_dir = 0

        if c == "D":
            temp = dice[d]
            dice[d] = dice[f]
            dice[f] = dice[u]
            dice[u] = dice[b]
            dice[b] = temp
            d_dir = 1
        
        if c == "L":
            temp= dice[d]
            dice[d] = dice[l]
            dice[l] = dice[u]
            dice[u] = dice[r]
            dice[r] = temp
            d_dir = 2

        if c == "U":
            temp = dice[d]
            dice[d] = dice[b]
            dice[b] = dice[u]
            dice[u] = dice[f]
            dice[f] = temp
            d_dir = 3
        arr[x][y] = dice[d]
    else:
        dice = ex
    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end=" ")
    #     print()
    # print()

result = 0

for i in range(n):
    for j in range(n):
        result += arr[i][j]

print(result)