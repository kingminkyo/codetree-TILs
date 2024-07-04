k, n = tuple(map(int, input().split()))
ans = []

def print_answer():
    for a in ans:
        print(a, end=" ") 
    print()

def choose(curr_num):

    if curr_num == n + 1:
        print_answer()
        return
    
    for i in range(1, k+1):
        ans.append(i)
        choose(curr_num+1)
        ans.pop()


choose(1)