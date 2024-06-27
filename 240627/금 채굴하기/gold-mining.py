n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


k = n-1 

def get_area(k):
    return k*k + (k+1 ) * (k+1)

def get_num_of_gold(x, y, k):
    result = 0
    for i in range(n):
        for j in range(n):
            if abs(x-i) + abs(y-j) <= k:
                result += arr[i][j]

    return result

max_gold = 0

for i in range(n):
    for j in range(n):
        for k in range(n+1):
            nog = get_num_of_gold(i, j, k)

            if nog * m >= get_area(k):
                max_gold = max(max_gold, nog)

print(max_gold)