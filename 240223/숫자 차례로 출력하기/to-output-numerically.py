num = int(input())

def count_up(n):
    if n == 0:
        return

    count_up(n - 1)
    print(n, end=" ")

def count_down(n):
    if n == 0:
        return

    print(n, end=" ")
    count_down(n - 1)

count_up(num)
count_down(num)