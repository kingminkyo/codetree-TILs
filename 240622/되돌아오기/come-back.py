n = int(input())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
d_dic = {
    "E":0,
    "S":1,
    "W":2,
    "N":3
}

x, y = 0, 0
cnt = 0
ok = False
for _ in range(n):
    word, num = input().split()
    num = int(num)

    for _ in range(num):
        x, y = x+dx[d_dic[word]], y+dy[d_dic[word]]
        cnt += 1
        
        if x == 0 and y == 0:
            ok = True
            break

    if ok:
        break
    
if ok:
    print(cnt)
else:
    print(-1)