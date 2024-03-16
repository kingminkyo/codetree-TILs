a, b = tuple(map(int, input().split()))

rec = [
    input().split()
    for _ in range(a)
]


first = rec[0][0]
count = 0
for i in range (1, a):
    for j in range (1, b):
        if rec[i][j] != first:
            for k in range (i+1, a-1):
                for l in range (j+1, b-1):
                    if rec[k][l] == first:
                        count +=1 

print(count)