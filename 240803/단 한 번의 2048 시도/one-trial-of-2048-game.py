arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

#중력
#합 
#중력 

def gravity():
    for i in range(4):
        temp = [0 for _ in range(4)]

        cnt = 0

        for j in range(3, -1, -1):
            if arr[j][i] != 0:
                temp[cnt] = arr[j][i]
                cnt += 1
        cnt = 0
        for j in range(3, -1, -1):
            arr[j][i] = temp[cnt]
            cnt += 1

def print_arr():
    for i in range(4):
        for j in range(4):
            print(arr[i][j], end=" ")
        print()
    print()


def same_num():
    for i in range(4):

        for j in range(3, 0, -1):
            if arr[j][i] == arr[j-1][i]:
                arr[j][i] *= 2
                arr[j-1][i] = 0
next_arr = [
        [0 for _ in range(4)]
        for _ in range(4)
    ]     
def rotate():
    for i in range(4):
        for j in range(4):
            next_arr[i][j] = 0
    
    for i in range(4):
        for j in range(4):
            next_arr[i][j] = arr[4 - j - 1][i]
    
    for i in range(4):
        for j in range(4):
            arr[i][j] = next_arr[i][j]

d_dir = input()

how_dir = {
    "D":0,
    "U":2,
    "R":1,
    "L":3
}

for _ in range(how_dir[d_dir]):
    rotate()

gravity()
same_num()
gravity()

for _ in range(4-how_dir[d_dir]):
    rotate()

print_arr()