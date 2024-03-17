import sys

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize


for i in range (1, n-1): # 1~2
    dist = 0
    x1 = arr[0][0]
    y1 = arr[0][1]
    for j in range(1, n): # 1~3 
        if j == i:
            continue
        dist += abs(x1 - (arr[j][0])) + abs(y1 - arr[j][1])
        x1 = arr[j][0]
        y1 = arr[j][1]
        
        # print(x1, y1)

    # if dist <= result:
    #     result = dist
    result = min(dist, result)

    

print(result)