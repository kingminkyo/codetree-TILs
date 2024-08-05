n = int(input())

ans = []

def print_ans():
    for a in ans:
        print(a, end="")
    print()

key = False

def is_okay():
    if key == True:
        return 
    length = 1
    while True:

        start1, end1 = len(ans) - length, len(ans) - 1
        start2, end2 = start1 - length, start1 - 1

        if start2 < 0:
            break

        if ans[start1:end1+1] == ans[start2:end2+1]:
            return False
        
        length+=1
    
    return True






def choose(num):
    global key 

    if num == n:

        print_ans()
        key = True 
        return 

    for i in range(4, 7):
        ans.append(i)   
        if is_okay():
            choose(num+1)
        ans.pop()

choose(0)