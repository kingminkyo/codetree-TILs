arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

d_dir = input()

def down_gravity():
    for i in range(4):
        temp = [0 for _ in range(4)]
        idx = 0
        for j in range(3, -1, -1):
            if arr[j][i] != 0:
                temp[idx] = arr[j][i]
                idx+=1
        
        for j in range(3, -1, -1):
            arr[j][i] = temp[3-j]

def up_gravity():
    for i in range(4):
        temp = [0 for _ in range(4)]
        idx = 0
        for j in range(0, 4):
            if arr[j][i] != 0:
                temp[idx] = arr[j][i]
                idx+=1
        
        for j in range(0, 4):
            arr[j][i] = temp[j]

def left_gravity():
    for i in range(4):
        temp = [0 for _ in range(4)]
        idx = 0
        for j in range(0, 4):
            if arr[i][j] != 0:
                temp[idx] = arr[i][j]
                idx+=1
        
        for j in range(0, 4):
            arr[i][j] = temp[j]

def right_gravity():
    for i in range(4):
        temp = [0 for _ in range(4)]
        idx = 0
        for j in range(3, -1, -1):
            if arr[i][j] != 0:
                temp[idx] = arr[i][j]
                idx+=1
        
        for j in range(3, -1, -1):
            arr[i][j] = temp[3-j]

def right_gob():
    for i in range(4):
        
        for j in range(3, 0, -1):

            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0

def left_gob():
    for i in range(4):
        
        for j in range(1, 4):

            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0

def up_gob():
    for j in range(4):
        
        for i in range(1, 4):

            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0

def down_gob():
    for j in range(4):
        
        for i in range(3, 1, -1):

            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0


if d_dir == "R":
    right_gravity()
    right_gob()
    right_gravity()

elif d_dir == "L":
    left_gravity()
    left_gob()
    left_gravity()


elif d_dir == "U":
    up_gravity()
    up_gob()
    up_gravity()

elif d_dir == "D":
    down_gravity()
    down_gob()
    down_gravity()

for i in range(4):
    for j in range(4):
        print(arr[i][j], end=" ")
    print()