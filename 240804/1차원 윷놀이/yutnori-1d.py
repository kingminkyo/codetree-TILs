n, m, k = tuple(map(int, input().split()))
# 4 6 3 

move = list(map(int, input().split()))
# 2 4 2 4 
board = []
for i in range(1, m+1):
    board.append(i)

ans = []

def print_ans():
    for a in ans:
        print(a, end=" ")
    print()



def score():
    horses = [ 1 for _ in range(k) ]
    get = [0 for _ in range(k)]
    # 1 1 1 
    result = 0 
    # move = 2 4 2 4 
    # ans = 0 0 0 0 
    for i in range(n):
        
        if horses[ans[i]] < m and not get[ans[i]]:
            horses[ans[i]] += move[i]
        
        if horses[ans[i]] >= m and not get[ans[i]]:
            result += 1 
            get[ans[i]] = 1 
            
    # print(horses)
        

    return result


result = 0
def choose(num):
    global result 
    if num == n:
        
        result = max(result, score())
        # print()
        return

    
    for i in range(k):
        ans.append(i)
        choose(num+1)
        ans.pop()

choose(0)
print(result)