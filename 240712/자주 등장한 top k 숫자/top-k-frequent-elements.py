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

numbers = [Number(key, value) for key, value in count.items()]

numbers.sort(key = lambda x: (-x.value, -x.keys))

for i in range(min(k, len(numbers))):
    print(numbers[i].keys, end=" ")