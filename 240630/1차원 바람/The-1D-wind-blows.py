class Wind:
    def __init__(self, row, direct):
        self.row = row 
        self.direct = direct 

winds = []

n, m, q = tuple(map(int, input().split()))

arr = [
    list(map( int, input().split()))
    for _ in range(n)
]

for _ in range(q):
    r, d = input().split()
    winds.append(Wind(int(r), d))

# 홀 짝 홀 짝 방향 계쏙 바뀌는 건 
# 위로 한 번, 아래로 한 번 

def wind_go(row, direct):
    if direct % 2 == 1:
        temp = arr[row][0]
        for i in range(m-1):
            arr[row][i] = arr[row][i+1]
        arr[row][m-1] = temp

    else:
        temp = arr[row][m-1]
        for i in range(m-1, 0, -1):
            arr[row][i] = arr[row][i-1]
        arr[row][0] = temp

def if_same(row, orin):
    
    for i in range(m):
        if arr[row][i] == arr[orin][i]:
            return True
    
    return False


for w in winds:
    row = w.row
    row = row - 1
    direct = 0

    if w.direct == "L":
        direct = 0
    else:
        direct = 1 

    wind_go(row, direct)
    
    n_dir = direct
    for i in range(row-1, 0-1, -1):
        n_dir += 1
        if if_same(i, i+1):
            wind_go(i, n_dir)
        else:
            break

    n_dir = direct

    for i in range(row+1, n):
        n_dir+=1
        if if_same(i, i-1):
            wind_go(i, n_dir)
        else:
            break

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()