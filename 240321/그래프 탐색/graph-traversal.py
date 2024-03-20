n, m = tuple(map(int, input().split()))

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
vertex_cnt = 0

for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(vertex):
    global vertex_cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            # print(curr_v)
            vertex_cnt+=1
            visited[curr_v] = True
            dfs(curr_v)

visited[1] = True
dfs(1)

print(vertex_cnt)