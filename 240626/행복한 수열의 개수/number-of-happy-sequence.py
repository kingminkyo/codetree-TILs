n, m = map(int,input().split())
m -= 1
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0

for i in range(n):
    count = 0
    for j in range(1, n):
        if arr[i][j] == arr[i][j-1]:
            count+= 1 
            # print(i, j, count)

        if count >= m:
            result += 1 
            break

for i in range(n):
    count = 0
    for j in range(1, n):
        if arr[j][i] == arr[j-1][i]:
            count+= 1 
            # print(i, j, count)

        if count >= m:
            result += 1 
            break

print(result)