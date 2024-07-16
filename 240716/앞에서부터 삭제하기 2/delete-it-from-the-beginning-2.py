from collections import deque 
import heapq as hq 

n = int(input())
arr = list(map(int, input().split()))


avg_max = 0

for _ in range(n-2):
    pq = []
    arr.pop(0)
    for a in arr:
        hq.heappush(pq, a)
    
    idx = 0
    pq_sum = 0
    avg = 0
    for i in range(1, len(pq)):
        idx += 1 
        pq_sum += pq[i]

    avg = pq_sum / idx
    avg_max = max(avg, avg_max)

print(f"{avg_max:.2f}")


# 3 1 9 2 7 
# k는 1에서 3까지 (1 ~ n-2)