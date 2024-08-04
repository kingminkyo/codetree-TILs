n = int(input())
lines = []

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    lines.append((a, b))

ans = []

def max_lines():

    paper = dict()

    for i in range(n):
        if ans[i] == 1:
            start, end = lines[i]
        else:
            continue
        
        for num in range(start, end+1):
            if num not in paper:
                paper[num] = 1
                # print(paper)
            else:
                # print(paper)
                return 0
    result = 0
    

    for a in ans:
        if a == 1:
            result += 1
        
    return result 





def print_ans():
    for a in ans:
        print(a, end="")

    print()

result = 0
def choose(num):
    global result 

    if num == n:
        # print_ans()
        result = max(result, max_lines())
        # print(result)
        return 

    for i in range(2):
        ans.append(i)
        choose(num+1)
        ans.pop()

choose(0)
print(result)