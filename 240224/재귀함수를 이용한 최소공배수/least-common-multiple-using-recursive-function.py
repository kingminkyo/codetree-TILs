num = int(input())
arr = list(map(int, input().split()))

def fun(n, a):
    if n == 0:
        return 1

    if fun(n-1, a) % a[n-1] == 0:
        return fun(n-1, a)
    else:
        return fun(n-1, a) * a[n-1]

    

print(fun(num,arr))