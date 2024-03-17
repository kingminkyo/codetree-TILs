n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

import sys
ans = sys.maxsize

# print(arr)
for i in range(n): # 0 1 2 3 4 
    far = 0
    dist = 0

    for j in range(i+1, n+i): # i가 2일 때 3 4 5 6 
        far+=1
        if j>(n-1):
            
            j = j-n
        # print(j)

        dist+=(arr[j] * far)
        # print(dist)

    ans = min(ans, dist)

print(ans)