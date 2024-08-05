n, m = tuple(map(int, input().split()))



ans = []

def print_ans():
    for a in ans:
        print(a, end=" ")
    print()

def choose(num, cnt):

    if num == n + 1 :
        if cnt == m:
            print_ans()
        return
    
    ans.append(num)
    choose(num+1, cnt+1)
    ans.pop()

    choose(num+1, cnt)

choose(1, 0)