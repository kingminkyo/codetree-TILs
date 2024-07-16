import heapq as hq

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_pq, min_pq = [], []
    median = arr[0]
    print(median, end=" ")
    for i in range(1, n):
        if i % 2 == 1:
            if arr[i] < median:
                hq.heappush(max_pq, -arr[i])
            else:
                hq.heappush(min_pq, arr[i])
        
        else:
            if len(max_pq) > len(min_pq):
                new_cand = -hq.heappop(max_pq)
            else:
                new_cand = hq.heappop(min_pq)
            
            nums = sorted([new_cand, arr[i], median])

            hq.heappush(max_pq, -nums[0])
            hq.heappush(min_pq, nums[2])
            median = nums[1]
            print(median, end=" ")





    
    print()