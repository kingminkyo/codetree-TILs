import heapq as hq

pq = []

n = int(input())

for _ in range(n):
    num = int(input())

    if num > 0:
        hq.heappush(pq, -num)
    elif num == 0 and len(pq) > 0 :
        print(-hq.heappop(pq))
    else:
        print(0)