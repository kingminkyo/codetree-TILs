n, m = map(int,input().split())
m -= 1
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

result = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if j>0 and arr[i][j] == arr[i][j-1]:
            cnt += 1
        else:
            cnt = 0
            # print(i, j)
        if cnt == m:
            result += 1 
            break
            
cnt = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if j>0 and arr[j][i] == arr[j-1][i]:
            cnt += 1
        else:
            cnt = 0 
            
        if cnt == m:
            result += 1 
            break


print(result)