num = int(input())

def shooting_star(n):
    if n == 0:
        return

    print("* " * n)
    shooting_star(n-1)
    print("* " * n)


shooting_star(num)