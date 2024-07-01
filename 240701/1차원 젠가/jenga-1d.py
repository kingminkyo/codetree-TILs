n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

start, end = tuple(map(int, input().split()))

start, end = start-1, end-1
# print(start, end)
for i in range(start, end+1):
    arr[i] = -1

temp = []
for a in arr:
    if not a == -1:
        temp.append(a)

arr = temp

# print(arr)
start, end = tuple(map(int, input().split()))

start, end = start-1, end-1
# print(start, end)
for i in range(start, end+1):
    arr[i] = -1

temp = []
for a in arr:
    if not a == -1:
        temp.append(a)
arr = temp


print(len(arr))
if len(arr) != 0:
    for a in arr:
        print(a, end="\n")