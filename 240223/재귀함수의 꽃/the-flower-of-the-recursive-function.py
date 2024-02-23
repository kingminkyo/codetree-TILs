numm = int(input())


def count(n):
    

    if n == 0:
        return

    print(n, end=" ")
    count(n-1)
    print(n, end=" ")


count(numm)