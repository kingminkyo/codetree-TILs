k , n = tuple(map(int, input().split()))

for i in range(1, k+1):
    for n in range(1, n+1):
        
        if k == 1 and n == 1:
            print(i)
            break
        else:
            print(f"{i} {n}")