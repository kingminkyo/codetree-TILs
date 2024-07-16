import heapq as hq 
n = int(input())
arr = list(map(int, input().split()))

pq = []

for i in range(n):

    hq.heappush(pq, arr[i])


    if i >= 2:
        h1 = hq.heappop(pq)
        h2 = hq.heappop(pq)
        h3 = hq.heappop(pq)
        print(h1 * h2 * h3)

        hq.heappush(pq, h1)
        hq.heappush(pq, h2)
        hq.heappush(pq, h3)
    else:
        print(-1)