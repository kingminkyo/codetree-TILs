n1 = int(input())
a = list(map(int, input().split()))


for i in range(n1):
    if a[i] % 2 == 0:
        a[i] //= 2
    

for i in range (n1):
    print(a[i], end=" ")