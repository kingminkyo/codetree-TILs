num = int(input())

def fun(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return fun(n//2) + 1
    
    else:
        return fun(n//3) + 1


print(fun(num))