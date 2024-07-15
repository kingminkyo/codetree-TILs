n, m = tuple(map(int, input().split()))

import heapq as hq
pq = []
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    num = abs(x) + abs(y)
    hq.heappush(pq, (num, x, y))

for _ in range(m):
    num, x, y = hq.heappop(pq)
    x, y = x+2, y+2
    num = abs(x) + abs(y)
    hq.heappush(pq, (num, x, y))

print(pq[0][1], pq[0][2])