n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

d = dict()
d[k] = 0

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == k:
            d[k] += 1

print(d[k])