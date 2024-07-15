n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

import heapq as hq
pq = []

for elem in arr:
    hq.heappush(pq, -elem)
    # print(pq)


for i in range(m):
    # print(pq)
    num = -hq.heappop(pq)
    num -= 1 

    hq.heappush(pq, -num)

print(-pq[0])