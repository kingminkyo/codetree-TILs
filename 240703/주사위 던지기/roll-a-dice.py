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

for c in commands:
    # U D R L 
    u, d, f, b, r, l = "u", "d", "f", "b", "r", "l"    
    

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
    
    x, y = x+dxs[d_dir], y+dys[d_dir]
    
    arr[x][y] = dice[d]


result = 0

for i in range(n):
    for j in range(n):
        result += arr[i][j]

print(result)