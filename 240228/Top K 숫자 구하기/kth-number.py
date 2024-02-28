n, k = tuple(map(int,input().split()))
arr = list(map(int, input().split()))
arr_sorted = sorted(arr)
print(arr_sorted[k-1])