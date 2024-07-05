n = int(input())

class Line:
    def __init__(self, x1, x2):
        self.x1, self.x2 = x1, x2
    def out():
        return self.x1, self.x2

lines = []

for _ in range(n):
    x, y = map(int, input().split())
    lines.append(Line(x, y))



lines.sort(key = lambda x: (-x.x1, -x.x2))

for line in lines:
    print(line.x1, line.x2)





ans = []

def print_ans():
    for a in ans:
        print(a, end=" ")
    print()
    
def collect_cnt():
    cnt = 0
    temp = []

    for idx, num in enumerate (ans):
        if num == 1:
            temp.append(lines[idx])
    
    temp.sort(key = lambda x: (x.x1, x.x2))
    info = [0 for _ in range(len(temp))]

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            
            if temp[i].x2 >= temp[j].x1:
                info[i], info[j] = 1, 1
                # print(info)
                # print(temp[i].x1, temp[i].x2, temp[j].x1, temp[j].x2)

    for i in info:
        if i == 0:
            cnt+=1
    # print("ans :", ans)
    # print("cnt:",cnt)
    return cnt

cnt = 0
def choose(curr_num):
    global cnt
    if curr_num == n:
        cnt = max(cnt, collect_cnt())
        
        return

    for i in range(0, 2):
        ans.append(i)
        choose(curr_num + 1)
        ans.pop()

# 000 001 010 011 100 101 110 111 

choose(0)