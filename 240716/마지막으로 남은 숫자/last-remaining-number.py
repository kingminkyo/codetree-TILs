import heapq as hq
n = int(input())
arr = list(map(int, input().split()))
pq = []
for a in arr:
    hq.heappush(pq, -a)




while len(pq) >= 2:
    fst = -hq.heappop(pq)
    sec = -hq.heappop(pq)

    cha = fst - sec

    if cha != 0:
        hq.heappush(pq, -cha)

if len(pq) > 0:
    print(-pq[0])
else:
    print(-1)