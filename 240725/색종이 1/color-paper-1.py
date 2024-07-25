n = int(input())

paper = []

arr = [
    [0 for _ in range(32)]
    for _ in range(32)
]

for _ in range(n):
    x, y = tuple(map(int, input().split()))

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

cnt = 0
for i in range(32):
    for j in range(32):
        if arr[i][j] == 1:
            cnt += 1
print(cnt )