a = input()

result = True
for i in range (len(a) // 2):
    for j in range (len(a) - i):
        if a[i] == a[i+j]:
            result = False


if result:
    print("No")
else:
    print("Yes")