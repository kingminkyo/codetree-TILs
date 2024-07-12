m, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = dict()

for a in arr:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1


new_arr = [
    [value, key]
    for key, value in count.items()
]

new_arr = sorted(new_arr)
leng = len(new_arr)

for i in range(leng-1, leng-k-1, -1):
    print(new_arr[i][1], end=" ")