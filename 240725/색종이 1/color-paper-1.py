n = int(input())

paper = []

arr = [
    [0 for _ in range(100)]
    for _ in range(100)
]
def in_range(x, y):
    return x>=0 and x<100 and y>=0 and y<100

for _ in range(n):
    x, y = tuple(map(int, input().split()))

    for i in range(x, x+10):
        for j in range(y, y+10):
            if in_range(i, j):
                arr[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt )