a = list(map(int, list(input())))



count = 0

for i in range(len(a)):
    if a[i] == 0:
        a[i] = 1
        count += 1 
        break

if count == 0:
    a[len(a)-1] = 0
num = 0


for i in range(len(a)):
    num = num * 2 + a[i]

print(num)