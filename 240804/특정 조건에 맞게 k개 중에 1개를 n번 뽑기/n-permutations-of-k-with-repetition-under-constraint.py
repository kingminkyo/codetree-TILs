k, n = tuple(map(int, input().split()))

ans = []

def print_ans():
    for a in ans:
        print(a, end=" ")
    print()

def choose(num):
    if num == n:
        print_ans()
        return
    
    for i in range(1, k+1):
        if num >= 2 and i == ans[len(ans)-1] and i == ans[len(ans)-2]:
            continue
        else:
            ans.append(i)   
            choose(num+1)
            ans.pop()

choose(0)