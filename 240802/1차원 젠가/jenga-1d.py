n = int(input())

block = []

for _ in range(n):
    block.append(int(input()))

def arrange():
    global block
    temp = []
    for b in block:
        if b != 0:
            temp.append(b)
    block = temp


for _ in range(2):
    start, end = tuple(map(int, input().split()))
    start, end = start-1, end-1 
    for i in range(start, end+1):
        block[i] = 0

    
    arrange()
    # print(block)

print(len(block))
for b in block:
    print(b)