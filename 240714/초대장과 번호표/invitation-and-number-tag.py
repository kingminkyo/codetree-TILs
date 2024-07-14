n, g = tuple(map(int, input().split()))

sets = set()

for _ in range(g):
    invites = list(map(int, input().split()))
    cnt = 0

    

    for i in range(1, invites[0] + 1):
        if invites[i] == 1 or invites[i] in sets:
            sets.add(invites[i])
            cnt += 1
        
    if (invites[0] - cnt) == 1:
         for i in range(1, invites[0] + 1):
            sets.add(invites[i])
    
print(len(sets))