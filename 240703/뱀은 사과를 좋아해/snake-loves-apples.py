n, m, k = map(int, input().split())

class Snake:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

class Command:
    def __init__(self, dct, num):
        self.dct = dct
        self.num = num 

# 격자 초기화
arr = [[0 for _ in range(n)] for _ in range(n)]

# 사과 위치 입력 받기
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1  # 0부터 시작하는 인덱스로 변환
    arr[x][y] = 1 

# 명령 입력 받기
commands = []
for _ in range(k):
    d, a = input().split()
    commands.append(Command(d, int(a)))

# 범위 체크 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 뱀의 몸통을 저장할 리스트
roots = []

# 디버깅을 위한 함수 (뱀의 현재 상태 출력)
def print_roots():
    print("root: ", end=" ")
    for root in roots:
        print(f"{root.x} {root.y} {root.num} / ", end=" ")
    print()
    print()

# 방향 설정 (우, 하, 좌, 상)
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
d_dir = 0

# 초기 위치 설정
x, y = 0, 0 
cnt = 0

# 뱀의 몸통을 정렬하는 함수 (num 기준 내림차순)
def root_sort():
    roots.sort(key=lambda s: -s.num)

# 명령 수행
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

    for _ in range(c.num):
        nx, ny = x + dxs[d_dir], y + dys[d_dir]
        if not in_range(nx, ny):
            cnt += 1
            is_gameover = True
            break

        # 사과 발견 시 
        if arr[nx][ny] == 1:
            roots.append(Snake(x, y, cnt))
            root_sort()
            x, y = nx, ny
            arr[nx][ny] = 0
            cnt += 1 
        else:
            if len(roots) != 0:
                roots.pop()
                roots.append(Snake(x, y, cnt))
                root_sort()
            x, y = nx, ny
            cnt += 1 

        # 뱀의 몸통과 부딪혔는지 체크
        for root in roots:
            if x == root.x and y == root.y:
                is_gameover = True
                break

    if is_gameover:
        break        

print(cnt)