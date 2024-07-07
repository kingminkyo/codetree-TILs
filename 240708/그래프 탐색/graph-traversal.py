n, m = tuple(map(int, input().split()))


arr = [
    [] for _ in range(n+1)
]
visited = [ False for _ in range(n+1)]

# print(arr)
cnt = 0
def dfs(x):
    global cnt

    for curr_num in arr[x]:

        if not visited[curr_num]:
            cnt += 1 
            visited[curr_num] = True
            dfs(curr_num)




visited[1] = True

for _ in range(m):
    x, y = tuple(map(int, input().split()))

    arr[x].append(y)
    arr[y].append(x)

dfs(1)
print(cnt)