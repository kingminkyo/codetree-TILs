num = int(input())

def fun(n):
    if n == 1 or n == 0:
        return 2

    
    return (fun(n-1) * fun(n-2)) % 100

print(fun(num))