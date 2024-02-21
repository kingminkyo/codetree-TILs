a, b = tuple(map(int, input().split()))

def sosu(x):
    if x <= 0:
        return False
    else:
        for i in range (2, x):
            if x % i == 0:
                return False

    return True

result = 0 

for i in range (a, b):
    if sosu(i):
        if (i //10 + i % 10 ) % 2 == 0:
            result += 1 


print(result)