n, m = tuple(map(int, input().split()))
ans = []

def print_combi():
    for a in ans:
        print(a, end=" ")
    print()

def choose(curr_num, cnt):
    if curr_num == n+1:

        if cnt == m:
            print_combi()
        return


    ans.append(curr_num)
    choose(curr_num+1, cnt+1)
    ans.pop()

    choose(curr_num+1, cnt)
        
    
choose(1, 0)