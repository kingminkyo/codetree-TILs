# n, m = tuple(map(int, input().split()))
# arr = tuple(map(int, input().split()))


# ans = []

# def print_ans():
#     for a in ans:
#         print(a, end="")
#     print()

# result = 0

# def find_xor():
#     global result

#     calc = 0

#     for i in range(len(ans)):
#         calc ^= arr[ans[i]]
    
#     result = max(result, calc)


# def choose(num, cnt):
#     # print_ans()
#     if cnt == m:
#         # print_ans()
#         find_xor()
#         return

#     if num == n:
#         return

#     ans.append(num)
#     choose(num+1, cnt+1)
#     ans.pop()
    
#     choose(num+1, cnt)

# choose(0, 0)

# print(result)
            




n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = []

def print_ans():
    for a in ans:
        print(a, end=" ")
    print()

def calc():
    collects = []
    result = 0

    for a in ans:
        collects.append(arr[a])
    
    result = collects[0]

    for i in range(1, len(collects)):
        result ^= collects[i]

    return result



result = 0 
def choose(curr_num, cnt):
    global result 

    if curr_num == n:
        if cnt == m:
            result = max(result, calc())
        return
    
    ans.append(curr_num)
    choose(curr_num+1, cnt+1)
    ans.pop()

    choose(curr_num+1, cnt)

choose(0, 0)
print(result)