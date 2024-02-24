a, b, c = tuple(map(int,input().split()))

su = a* b* c
def fun (n):
    if n // 10 == 0:
        return n

    return fun(n//10) + n%10


print(fun(su))