n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

happy = 0 

for i in range(n):
    same = 0
    for j in range(1, n):
        if grid[i][j] == grid[i][j-1]:
            # print(f"{i} {j}")
            same+= 1
        
        if same >= m-1:
            happy+=1
            break

        if grid[i][j] != grid[i][j-1]:
            same = 0



if n == 1 and grid[0][0] == 1:
    happy = 2


for i in range(n):
    same = 0
    for j in range(1, n):
        if grid[j][i] == grid[j-1][i]:
            # print(f"{i} {j}")
            same+= 1

        if same >= m-1:
            happy+=1
            break

        if grid[j][i] != grid[j-1][i]:
            same = 0

    

print(happy)