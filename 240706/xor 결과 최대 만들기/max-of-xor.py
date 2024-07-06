n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0

# 총 n개, 그리고 m개 조합 

def choose(curr_idx, cnt, curr_val):
    global ans

    if cnt == m:
        ans == max(ans, curr_val)
        return
    
    if curr_idx == n:
        return

    choose(curr_idx + 1, cnt, curr_val)
    choose(curr_idx + 1, cnt + 1, curr_val ^ arr[curr_idx])


choose(0, 0, 0)
print(ans)