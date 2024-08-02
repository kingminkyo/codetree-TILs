n, m, q = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# to가 0이면 왼쪽에서, 1이면 오른쪽에서 

def wind(row, to):
    if to == 0:
        temp = arr[row][m-1]
        for i in range(m-1, 0, -1):
            arr[row][i] = arr[row][i-1]
        arr[row][0] = temp

    else:
        temp = arr[row][0]
        for i in range(m-1):
            arr[row][i] = arr[row][i+1]
        arr[row][m-1] = temp

def print_arr():
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print()


def wind_up(row, to):

    for i in range(row-1, -1, -1):
        to = (to+1) % 2 
        key = False

        for j in range(m):
            if arr[i][j] == arr[i+1][j]:
                key = True
                wind(i, to)
                break

        if key == False:
            return


def wind_down(row, to):
    for i in range(row+1, n):
        to = (to+1) % 2 
        key = False

        for j in range(m):
            if arr[i][j] == arr[i-1][j]:
                key = True
                wind(i, to)
                # print_arr()
                # print(i, j)
                break

        if key == False:
            return


for _ in range(q):
    row, to = input().split()
    row = int(row) -1 
    if to == "L":
        to = 0
    else:
        to = 1

    wind(row, to)

    wind_up(row, to)

    wind_down(row, to)
    
print_arr()