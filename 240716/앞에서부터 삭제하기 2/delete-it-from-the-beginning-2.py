import heapq as hq 

n = int(input())
arr = list(map(int, input().split()))

sum_val = 0
max_avg = 0
pq = []

sum_val += arr[n-1]
hq.heappush(pq, arr[n-1])
# k는 1에서 3까지 (1 ~ n-2)

for i in range(n-2, 0, -1):

    hq.heappush(pq, arr[i])
    sum_val += arr[i]

    
    avg = (sum_val - pq[0]) / (len(pq) - 1)

    max_avg = max(avg, max_avg)
    
    # print(pq, avg, sum_val)

print(f"{max_avg:.2f}")