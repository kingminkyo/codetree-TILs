n = int(input())
# n = 7
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

        elif result[i] >= 1 and len(double_stack) != 0 and double_stack[len(double_stack)-1] != result[i]:
            break


        elif result[i] >= 2 and  (double_stack[len(double_stack)-1] != result[i] or result[i-1] != result[i]):
            for j in range(result[i]-1):
                double_stack.append(result[i])

        
        
        elif len(double_stack) != 0 and result[i-1] == result[i] and result[i] != 1:
            double_stack.pop()        
    # print(double_stack)

    if len(double_stack) == 0:
        double_stack = []
        return True
    else:
        double_stack = []
        return False

# def is_beautiful():
#     i = 0
#     for i in range(0, n, result[i]):
#         if result[i] > n:
#             return False
#         for j in range(i, i + result[i]):
#             if result[i] != result[j]:
#                 return False
        
        
#     return True
def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡습니다.
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 아름다운 수가 아닙니다.
        if i + result[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인합니다.
        # 하나라도 다른 숫자가 있다면
        # 아름다운 수가 아닙니다.
        for j in range(i, i + result[i]):
            if result[j] != result[i]:
                return False
            
        i += result[i]
        
    return True

end = 0
def find_bt(cnt):
    global end
    if cnt == n+1:
        # print_bt()
        
        if is_beautiful():
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