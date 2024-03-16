import sys
a = input()

count = 0
for i in range(len(a)):
    for j in range(i+1 , len(a)):
        if a[i] == "(" and a[j] == ")":
            count += 1

    
print(count)