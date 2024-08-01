n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0

for i in range(n):
    cnt = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            cnt += 1
        else:
            cnt = 1
        
        if cnt == m:
            result += 1
            continue

for i in range(n):
    cnt = 1
    for j in range(n-1):
        if arr[j+1][i] == arr[j][i]:
            cnt += 1
        else:
            cnt = 1
        
        if cnt == m:
            result += 1
            continue
print(result)