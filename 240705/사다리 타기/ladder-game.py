n, m = tuple(map(int, input().split()))
lines = []
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a-1))

lines.sort()

temps = []
cnt = 0 

def check():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]

    for _, idx in lines:
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]

    for _, idx in temps:
        num2[idx], num2[idx+1] = num2[idx+1], num2[idx]

    for i in range(n):
        if num1[i] != num2[i]:
            return 1000000000
    
    return len(temps)

cnt = m 
def choose(curr_num):
    global cnt 

    if curr_num == m:
        cnt = min(cnt, check())

        return
    
    temps.append(lines[curr_num])
    choose(curr_num+1)
    temps.pop()

    choose(curr_num+1)

choose(0)
print(cnt)