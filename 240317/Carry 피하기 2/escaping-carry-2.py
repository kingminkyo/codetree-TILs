n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


import sys
ans = -sys.maxsize

def carry(a, b):
    a1000 = a // 1000
    b1000 = b // 1000

    a100 = (a-a1000*1000 ) // 100
    b100 = (b-b1000*1000 ) // 100

    a10 = (a-a1000*1000-a100*100) // 10
    b10 = (b-b1000*1000-b100*100) // 10

    a1 = a-a1000*1000-a100*100-a10*10
    b1 = b-b1000*1000-b100*100-b10*10

    if a1000+b1000 >= 10 or a100+b100 >= 10 or a10+b10 >=10 or a1+b1 >= 10:
        return True
    return False

for i in range(n):
    for j in range(i+1, n):
        if carry(arr[i], arr[j]) is False:
            for k in range(j+1, n):

                if carry((arr[i]+arr[j]), arr[k]) is False:
                    no = arr[i]+arr[j]+ arr[k]
                    # print (f"{arr[i]} {arr[j]} {arr[k]}")
                    ans = max(ans,no)

if ans < 0:
    ans = -1
print(ans)