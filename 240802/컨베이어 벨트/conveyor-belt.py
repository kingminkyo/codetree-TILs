n, t = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

for _ in range(t):
    temp = arr[0][n-1]
    for i in range(n-1, -1, -1):
        arr[0][i] = arr[0][i-1]

    arr[0][0] = arr[1][n-1]

    for i in range(n-1, -1, -1):
        arr[1][i] = arr[1][i-1]
    arr[1][0] = temp
    

for i in range(2):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()