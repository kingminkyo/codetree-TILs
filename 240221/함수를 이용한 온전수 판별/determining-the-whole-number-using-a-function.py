a, b = tuple(map(int, input().split()))

def onsu(a):
    if a%2 == 0:
        return False
    if a%10 == 5:
        return False
    if a % 3 == 0 and a % 9 != 0:
        return False
    # print(a)
    return True 

result = 0 
for i in range(a, b+1):
    if onsu(i):
        result += 1

print(result)