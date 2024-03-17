a = input()
dep = len(a)

count = 0
for i in range(len(a)):
    if i != 0 and a[i] == "(" and a[i-1] == "(":
        
        for j in range (i+1, dep):
            if a[j] == ")" and a[j-1] == ")":
                count +=1

print(count)