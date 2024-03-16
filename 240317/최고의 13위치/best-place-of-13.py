n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))\

result = 0
for i in range(n):
    for j in range(n-2):
        count = arr[i][j] + arr[i][j+1] + arr[i][j+2]

        result = max(result, count)


print(result)