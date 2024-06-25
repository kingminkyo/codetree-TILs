n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x>= 0 and x<n and y>=0 and y<n

result = 0
count = 0
for i in range(n-2):
    for j in range(n-2):
        for a in range(3):
            for b in range(3):
                if in_range(i+a, i+b):

                    count = count + arr[i+a][i+b]       
                # print (count, i, j, i+a, j+b)
        
        
        if count > result:
            result = count
        count = 0

print(result)