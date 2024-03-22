n = int(input())
# n = 4
result = []

def print_bt():
    for i in result:
        print(i, end="")

    print()

double_stack = []
# print(len(double_stack))

def check_double():
    global double_stack
    for i in range(n): # 0부터 탐색

        # 2 4 2 를 가정하자 
        if len(double_stack) == 0 and result[i] >= 2 :
            for j in range(result[i]-1):
                double_stack.append(result[i])


        elif result[i] >= 2 and  double_stack[len(double_stack)-1] != result[i]:
            for j in range(result[i]-1):
                double_stack.append(result[i])
        
        elif len(double_stack) != 0 and result[i-1] == result[i] and result[i] != 1:
            double_stack.pop()
        
        else:
            for j in range(result[i]-1):
                double_stack.append(result[i])
        
    # print(double_stack)

    if len(double_stack) == 0:
        double_stack = []
        return True
    else:
        double_stack = []
        return False




end = 0
def find_bt(cnt):
    global end
    if cnt == n+1:
        # print_bt()
        
        if check_double():
            # print_bt()
            # print(double_stack)
            end+=1
        return

    for i in range(1, 5):
        result.append(i)

        find_bt(cnt+1)
        result.pop()

find_bt(1)

print(end)