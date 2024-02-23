num = int(input())

def starr(n):
    if n == 0:
        return
    starr(n - 1)
    print("*" * n)

starr(num)