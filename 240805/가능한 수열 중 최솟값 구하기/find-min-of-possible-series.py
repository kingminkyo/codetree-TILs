n = int(input())

ans = []

def print_ans():
    for a in ans:
        print(a, end="")
    print()

key = False

def choose(num):
    global key 

    if num == n:

        print_ans()
        key = True 
        return 

    for i in range(4, 7):
        if key == True:
            break 
        if num >= 1:
            if ans[-1] == i:
                continue
        if num >= 3:
            if ans[-3] == ans[-1] and ans[-2] == i:
                continue
        if num >= 5:
            if ans[-5] == ans[-2] and ans[-4] == ans[-1] and ans[-3] == i:
                continue
                
            

        ans.append(i)
        choose(num+1)
        ans.pop()

choose(0)