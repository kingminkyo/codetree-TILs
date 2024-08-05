n, m = tuple(map(int, input().split()))

points = []

for _ in range(n):
    r, c = tuple(map(int, input().split()))
    points.append((r, c))

import math 
import sys

def ucd():
    
    distance = 0


    result = 0

    for i in range(len(ans)-1):
        for j in range(i+1, len(ans)):
            x1, y1 = points[ans[i]]
            x2, y2 = points[ans[j]]
            distance = abs((x1-x2)**2 + (y1-y2)**2)

            result = max(result, distance)



    return result




ans = []


result = sys.maxsize

def choose(num, cnt):
    global result 

    if cnt == m:
        # print(ans)
        # print(ucd())
        result = min(ucd(), result)
        return

    if num == n:
        return 

    ans.append(num)
    choose(num+1, cnt+1)
    ans.pop()

    choose(num+1, cnt)

choose(0, 0)

print(result)