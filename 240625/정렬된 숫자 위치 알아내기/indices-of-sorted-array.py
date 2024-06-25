n = int(input())
arr = list(map(int, input().split()))

class Num:
    def __init__(self, n, i):
        self.n, self.i = n, i
        
i = 1
orin = []
nums = []

for a in arr:
    nums.append(Num(a, i))
    i+=1 
i = 1
for a in arr:
    orin.append(Num(a, i))
    i+=1 

nums.sort(key = lambda x:x.n)

for a in orin:
    for ii, n in enumerate(nums, start=1):
        # print(a.i)
        if a.i == n.i:
            print(f"{ii}", end=" ")