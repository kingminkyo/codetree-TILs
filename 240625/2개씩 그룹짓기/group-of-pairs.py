n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

i = 2
a1 = []
a2 = []

for a in arr:
    if i == 0:
        a1.append(a)
    elif i  == 1:
        a2.append(a)
    elif i  == 2:
        a2.append(a)
    else:
        a1.append(a)
    i = (i + 1) % 4

a1sum = 0
a2sum = 0

for (a, b) in zip(a1, a2):
    a1sum += a
    a2sum += b

result = 0

if  a1sum > a2sum:
    result = a1sum
else:
    result = a2sum
print(result)