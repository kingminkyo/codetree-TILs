n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
comp = list(map(int, input().split()))

for c in comp:
    result = 0

    for a in arr:
        if a == c:
            result += 1
    
    print(result, end=" ")