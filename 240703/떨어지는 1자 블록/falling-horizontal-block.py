n, m, k = tuple(map(int, input().split()))

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

k -= 1 

for i in range(k, k+m):
    arr[0][i] = 1


def rain():
    for i in range(1, n):
        cnt = 0
        for j in range(k, k+m):
            if arr[i][j] == 0:
                cnt += 1
            else:
                break
        
        if cnt >= m:
            for j in range(k, k+m):
                arr[i][j] = 1
                arr[i-1][j] = 0
        else:
            break

        



rain()
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()