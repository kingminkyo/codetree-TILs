n = int(input())
arr = list(map(int,input().split()))

arr.sort()

group_a = []
group_b = []

# print(arr)

for i in range(n*2):
    # print(i)
    if i % 2 == 0 or i == 0:
        group_a.append(arr[i])
    else:
        group_b.append(arr[n*2-i])


result = 0
for i in range(n):
    result += group_b[i]


print(group_b)