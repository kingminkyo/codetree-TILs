n = int(input())

visited = [0 for _ in range(n+1)]

ans = []

def choose(num):
    if num == n:
        for a in ans:
            print(a, end=" ")
        print()
        

    for i in range(n, 0, -1):
        if visited[i] == 1:
            continue
        
        ans.append(i)
        visited[i] = 1

        choose(num+1)

        ans.pop()
        visited[i] = 0

choose(0)