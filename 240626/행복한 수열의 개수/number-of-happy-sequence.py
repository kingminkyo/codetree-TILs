n, m = map(int,input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0


for i in range(n):
    count = 1
    for j in range(1, n):
        if arr[i][j] == arr[i][j-1]:
            count+= 1 

    result = max(count, result)


print(result)