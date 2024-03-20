import sys

n = int(input())
arr = list(map(int, input().split()))

min_score = sys.maxsize

result = 0

def score(removed_idx):
    sum_val = 0
    prev = -1

    for i in range(n):
        if i == removed_idx:
            continue
        
        if prev != -1:
            sum_val += abs(arr[i] - prev)
        
        prev = arr[i]

    return sum_val
        


for i in range(n):
    arr[i] *= 2
    
    for j in range(n):
        min_score = min(min_score, score(j))


    
    arr[i] //= 2

print(result)