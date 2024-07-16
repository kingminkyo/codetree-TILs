n, m, k = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

import heapq as hq
pq = []

for i in range(n):
    hq.heappush(pq, (arr1[i]+arr2[0], i, 0 ))

for i in range(k-1):
    _, idx1, idx2 = hq.heappop(pq)

    idx2 += 1

    if idx2<m:
        hq.heappush(pq, (arr1[idx1] + arr2[idx2], idx1, idx2))

pair, _, _ = hq.heappop(pq)
print(pair)