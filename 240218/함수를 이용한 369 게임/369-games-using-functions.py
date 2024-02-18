def yes369(n):
    while (n>0):
        if n % 10 == 3 or n % 10 == 6  or n % 10 == 9 :
            return True
        
        n = n // 10

    return False

def basu3(n):
    return n % 3 == 0



a, b = tuple(map(int, input().split()))

result = 0
for i in range(a, b+1):
    if yes369(i) or basu3(i):
        # print(i)
        result += 1
    
print(result)