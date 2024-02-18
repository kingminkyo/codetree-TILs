def yes(n):
    return ((n % 2) == 0) and ( ((int(n/10) + n%10) % 5 )== 0)


a = tuple(map(int, input().split()))

print(yes(a))