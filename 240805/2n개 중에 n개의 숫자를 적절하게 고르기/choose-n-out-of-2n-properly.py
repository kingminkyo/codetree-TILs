n = int(input())
arr = list(map(int, input().split()))




ans = []

def compare():
    demo = []
    for a in arr:
        demo.append(a)

    score1, score2 = 0, 0 
    
    team1, team2 = [],[]

    for a in ans:
        team1.append(demo[a])
        demo[a] = 0
    for d in demo:
        if d != 0:
            team2.append(d)

    for s in team1:
        score1 += s
    for s in team2:
        score2 += s 
    
    return abs(score2-score1)

        
import sys
result = sys.maxsize

def choose(num, cnt):
    global result 
    if cnt == n:
        result = min(result, compare())        
        
        return

    if num == len(arr):
        return

    ans.append(num)
    choose(num+1, cnt+1)
    ans.pop()

    choose(num+1, cnt)

choose(0, 0)