a = input()


for i in range (len(a) // 2):
    for j in range (len(a) - i):
        if a[i] == a[i+j]:
            print("No")


print("Yes")