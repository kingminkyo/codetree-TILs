m, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = dict()

for a in arr:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

class Number:
    def __init__(self, keys, value):
        self.keys = keys
        self.value = value

numbers = []
for k, v in count.items():
    numbers.append(Number(k, v))

numbers.sort(key = lambda x: (-x.value, -x.keys))

for i in range(k):
    print(f"{numbers[i].keys}", end=" ")