nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
arr = list(map(int, input().split()))
arr_sorted = sorted(arr)
print(arr_sorted[k-1])