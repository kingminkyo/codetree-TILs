n = int(input())
arr = list(map(int, input().split()))

import sys
result = n+1 

def find_path(index, cnt):
    global result 

    if index >= (n-1):

        result = min(result, cnt)
        return

    if arr[index] == 0:
        return 

    for i in range(1, arr[index]+1):
        # print(index, cnt)
        find_path(index+i, cnt+1)
    
    
find_path(0, 0)



if result == (n+1):
    print(-1)
else:
    print(result)