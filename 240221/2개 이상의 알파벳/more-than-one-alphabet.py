a = input()

result = False
for i in range (len(a) // 2):
    count = 0
    for j in range (len(a) - i):
        if a[i] != a[i+j]:
            count += 1
        if count >= 2:
            result = True

if result:
    print("Yes")
else:
    print("No")