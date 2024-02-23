num = int(input())

def fun(n):
    if n == 2:
        return 2

    elif n == 1:
        return 1

    
    return fun(n-2) + n


print(fun(num))