n = int(input())
arr = list(map(int, input().split()))

arr.sort()

g_max = 0

for i in range(n):
    g_sum = arr[i] + arr[2*n -1 -i]
    if g_max < g_sum:
        g_max = g_sum

print(g_max)