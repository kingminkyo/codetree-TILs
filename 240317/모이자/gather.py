import sys

n = int(input())
a = list(map(int, input().split()))


dist = sys.maxsize
new = 0

for i in range(n):
    for j in range(n):
        new += (a[j] * abs(j-i))

    if new < dist:
        dist = new
    new = 0

print(dist)