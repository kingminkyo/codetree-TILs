m, limit = tuple(map(int, input().split()))
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
# numbers = [Number(k, v ) for k, v in count.items()]
for k, v in count.items():
    numbers.append(Number(k, v))

numbers.sort(key = lambda x: (-x.value, -x.keys))
# print(count)
# print(len(numbers))
for i in range(limit):
    
    print(numbers[i].keys, end=" ")