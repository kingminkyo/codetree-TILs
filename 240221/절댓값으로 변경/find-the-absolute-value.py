n1 = int(input())
a = list(map(int, input().split()))

for i in range(n1):
    if a[i] < 0:
        a[i] = -a[i]

    print(a[i], end=" ")