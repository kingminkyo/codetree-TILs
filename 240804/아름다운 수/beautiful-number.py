n = int(input())


ans = []

def check_beautiful():
    cnt = 1 
    for i in range(n-1):
        if ans[i] == ans[i+1]:
            cnt += 1
        else:
            if cnt % ans[i] == 0:
                cnt = 1
            else:
                return False
    if cnt % ans[n-1] != 0:
        return False
    
    return True


def print_ans():
    for a in ans:
        print(a, end="")
    print()



result = 0 
def choose(num):
    global result 
    if num ==  n:
        if check_beautiful():
            result += 1

        return

    for i in range(1, 5):
        ans.append(i)
        choose(num+1)
        ans.pop()

choose(0)
print(result)