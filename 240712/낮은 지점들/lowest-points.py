n = int(input())

count = dict()

for _ in range(n):
    x, y = tuple(map(int, input().split()))
    if x in count:
        if count[x] > y:
            count[x] = y
    else:
        count[x] = y
ans = 0
for x, y in count.items():
    ans += y

print(ans)