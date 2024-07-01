class Wind:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2


n, m, q = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

winds = []
for _ in range(q):
    a, b, c, d = tuple(map(int, input().split()))
    winds.append(Wind(a-1, b-1, c-1, d-1))

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

dxs, dys =[0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

sub = [
    [0] * m
    for _ in range(n)
]

def to_same():
    for i in range(n):
        for j in range(m):
            sub[i][j] = arr[i][j]

def rolling(x1, y1, x2, y2):
    temp1 = arr[x1][y2]
    temp2 = arr[x2][y2]
    temp3 = arr[x2][y1]
    
    for i in range(y2, y1, -1):
        arr[x1][i] = arr[x1][i-1]

    for i in range(x2, x1, -1):
        arr[i][y2] = arr[i-1][y2]

    for i in range(y1, y2):
        arr[x2][i] = arr[x2][i+1]

    for i in range(x1, x2):
        arr[i][y1] = arr[i+1][y1]

    arr[x1+1][y2] = temp1
    arr[x2][y2-1] = temp2
    arr[x2-1][y1] = temp3

    to_same()

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            num = 0
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny):
                    num += sub[nx][ny]
                    cnt += 1 
                    # print(num, cnt)
            arr[i][j] = int(num/cnt)





    
for w in winds:
    rolling(w.x1, w.y1, w.x2, w.y2)
    






for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()