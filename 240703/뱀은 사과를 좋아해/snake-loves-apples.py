n, m, k = tuple(map(int, input().split()))

class Snake:
    def __init__(self, x, y, num):
        self.x, self.y , self.num = int(x), int(y), int(num )
        
class Command:
    def __init__(self, dct, num):
        self.dct = dct
        self.num = num 

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1 
    arr[x][y] = 1 

commands = []



for _ in range(k):
    d, a = input().split()
    commands.append(Command(d, int(a)))

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

roots = []

def print_roots():
    print("root: ", end=" ")
    for root in roots:
        print(f"{root.x} {root.y} {root.num} / ", end=" ")
    print()
    print()


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
d_dir = 0

x, y = 0, 0 
cnt = 0
# print(type(cnt))
def root_sort():
    roots.sort(key= lambda x: -x.num)

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
        # print(cnt)
        nx, ny = x+dxs[d_dir], y+dys[d_dir]
        # print(c.dct, i)
        if not in_range(nx, ny):
            print("아웃")
            cnt+= 1
            is_gameover = True
            break

        # 사과 발견 시 

        if arr[nx][ny] == 1:
            
            roots.append(Snake(x, y, cnt))
            root_sort()
            x, y = nx, ny
            arr[nx][ny] = 0
            cnt += 1 
            # print("eat", x, y)
            # print_roots()
            

        else : 
            if len(roots) != 0:
                roots.pop()
                roots.append(Snake(x, y, cnt))
                root_sort()
            x, y = nx, ny
            # if cnt>=28:
            #     print(x, y)
            cnt += 1 
            # print_roots()

        #꼬리랑 겹치는 경로인지 탐색 
        for root in roots:
            # if cnt>=33:
            #     print()
            #     print("체크")
            #     print(x, y)
            #     print(f"{root.x} {root.y}")
            if x == root.x and y == root.y:
                # print("게임 오버")
                is_gameover = True
                break
            # else:
            #     print(f"아니지롱 {root.x} {root.y}")

    if is_gameover:
        break        

print(cnt)