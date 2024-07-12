n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

d = dict()


ans = 0

for a in arr:
    diff = k - a 

    if diff in d:
        ans += d[diff]

    if a in d:
        d[a] += 1
    else:
        d[a] = 1

print (ans)