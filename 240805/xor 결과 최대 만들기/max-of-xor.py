n, m = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))


ans = []

def print_ans():
    for a in ans:
        print(a, end="")
    print()

result = 0

def find_xor():
    global result

    calc = 0

    for i in range(len(ans)):
        calc ^= arr[ans[i]]
    
    result = max(result, calc)


def choose(num, cnt):
    # print_ans()
    if cnt == m:
        # print_ans()
        find_xor()
        return

    if num == n:
        return

    ans.append(num)
    choose(num+1, cnt+1)
    ans.pop()
    
    choose(num+1, cnt)

choose(0, 0)

print(result)