n = int(input())
import heapq as hq


max_pq, min_pq = [], []
for _ in range(n):
    num = int(input())

    if num > 0:
        hq.heappush(max_pq, num)
    elif num < 0:
        hq.heappush(min_pq, -num)
    
    
    elif num == 0:
        if len(max_pq) == 0 and len(min_pq) == 0:
            print(0)


        elif len(max_pq) == 0:
            print(-hq.heappop(min_pq))

        elif len(min_pq) == 0:
            print(hq.heappop(max_pq))
        elif min_pq[0] > max_pq[0]:
            print(hq.heappop(max_pq))
        elif min_pq[0] < max_pq[0]:
            print(-hq.heappop(min_pq))
        else:
            print(-hq.heappop(min_pq))
    # print(max_pq, min_pq)