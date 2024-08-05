n = int(input())
arr = [
    input()
    for _ in range(n)
]

# print(arr)

count = 0
book = dict()

for i in range(n):
    for j in range(n):
        # print(arr[i][j], end=" ")
        if arr[i][j] != "." and  arr[i][j] != "S" and  arr[i][j] != "E":
            count +=1
            num = int(arr[i][j])
            book[num] = (i, j)
        else:
            book[arr[i][j]] = (i, j)
            

ans = []

def count_range():
    x1, y1  = book["S"]
    length = 0
    x2, y2 = 0, 0
    for a in ans:
        x2, y2 = book[a]

        length = length + abs(x2-x1) + abs(y2-y1)
        x1, y1 = x2, y2

    x2, y2 = book["E"]

    length = length + abs(x2-x1) + abs(y2-y1)
    
    return length

# print(cnt)
import sys
result = sys.maxsize

def choose(num, cnt):
    global result
    if cnt == 3:
        # print(ans)
        result = min(result, count_range())
        return
    if num == count:
        
        return
    
    
    ans.append(num+1)
    choose(num+1, cnt+1)
    ans.pop()

    choose(num+1, cnt)


choose(0, 0)
if count < 3:
    print(-1)
else:
    print(result)