import heapq as hq 
n = int(input())
arr = list(map(int, input().split()))

pq = []

for i in range(n):

    hq.heappush(pq, arr[i])


    if i >= 2:
        print(pq[0] * pq[1] * pq[2])    
    else:
        print(-1)