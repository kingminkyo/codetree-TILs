n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))


ans = []
def print_ans():
    for a in ans:
        print(a, end=" ")
    print()


def check_xor():
    num = []
    for i in ans:
        num.append(arr[i-1])

    result = num[0]

    for i in range(1, len(num)):
        result = result ^ num[i]

    
    return result

final = 0 
def choose(curr_num, cnt):
    global final

    if curr_num == n+1:
        if cnt == m:
            final = max(final, check_xor())
        return

    ans.append(curr_num)
    choose(curr_num+1, cnt+1)
    ans.pop()

    choose(curr_num+1, cnt)

choose(0, 0)
print(final)