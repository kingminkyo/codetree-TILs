num = int(input())

def fun(n):
    if n == 1 or n == 0 :
        return 1

    return fun(n//3) + fun(n-1)


print(fun(num))