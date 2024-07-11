n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
comp = list(map(int, input().split()))

freq = dict()

for a in arr:
    if a not in freq:
        freq[a] = 1
    else:
        freq[a] += 1

for c in comp:
    if c not in freq:
        print(0, end=" ")
    else:
        print(freq[c], end=" ")