num = int(input())

def starr(n):
    if n == 0:
        return
    print("*" * n)
    starr(n - 1)

starr(num)