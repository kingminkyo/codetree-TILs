n = int(input())
arr = list(map(int, input().split()))

m = n*2 


ans = []


def print_ans():
    for a in ans:
        print(a, end=" ")
    print()

def cal_sum():
    num1, num2 = [], []
    temp = []
    for a in arr:
        temp.append(a)

    for i in ans:
        num1.append(temp[i])
    
    for i in ans:
        temp[i] = 0


    
    sum1, sum2 = 0, 0

    for a in num1:
        sum1 += a 
    for a in temp:
        sum2 += a
    
    return abs(sum1-sum2)


final = 10000000

def choose(curr_num, cnt):
    global final
    if curr_num == m:
        if cnt == n:
            
            final = min(final, cal_sum())

        return 

    ans.append(curr_num)
    choose(curr_num+1, cnt+1)
    ans.pop()
    
    choose(curr_num+1, cnt)

choose(0, 0)
print(final)