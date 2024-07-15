import heapq as hq

n = int(input())
pq = []

for _ in range(n):
    num = int(input())
    

    if num != 0:
        hq.heappush(pq, num)
    elif len(pq) > 0 :
        print(pq[0])
        hq.heappop(pq)
    elif len(pq) == 0 and num == 0:
        print(0)