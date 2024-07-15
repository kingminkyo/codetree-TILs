import heapq as hq

n = int(input())
pq = []

for _ in range(n):
    num = int(input())
    hq.heappush(pq, num)

    print(pq[0])