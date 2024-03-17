n = int(input())
arr = list(map(int, input().split()))

print(arr)

import sys
comp = -sys.maxsize

for i in range(n):
    cost = 0
    for j in range(i+2, n+i):
        
        if j>=n:
            j-=n

        
        if abs(i-j)>=2:
            cost=arr[i]+arr[j]
            comp = max(cost, comp)
            # print(cost)


print(comp)