n, m, k = tuple(map(int, input().split()))

class Snake:
    def __init__(self, x, y, num):
        self.x, self.y , self.num = x, y, num 
class Command:
    def __init__(self, dct, num):
        self.dct = dct
        self.num = num 

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x, y = int(input())
    x, y = x-1, y-1 
    arr[x][y] = 1 

commands = []

for _ in range(k):
    d, a = input().split()
    commands.append(Command(d, int(a)))

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

roots = []

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
d_dir = 0

x, y = 0, 0 
cnt = 0
# print(type(cnt))
def root_sort():
    roots.sort(key= lambda x: x.num)

for c in commands:
    
    if c.dct == "R":
        d_dir = 0
    elif c.dct == "D":
        d_dir = 1
    elif c.dct == "L":
        d_dir = 2
    elif c.dct == "U":
        d_dir = 3

    is_gameover = False 

    for i in range(c.num):
        nx, ny = x+dxs[d_dir], y+dys[d_dir]

        if not in_range(nx, ny):
            is_gameover = True
            break

        # 사과 발견 시 

        if arr[nx][ny] == 1:
            
            roots.append(Snake(x, y, cnt))
            root_sort()
            x, y = nx, ny
            arr[nx][ny] = 0
            cnt += 1 
        else : 
            if len(roots) != 0:
                roots.pop()
                roots.append(Snake(x, y, cnt))
                root_sort()
            x, y = nx, ny
            
            cnt += 1 

        


    


print(cnt)