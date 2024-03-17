arr = input()
arr = input()
dep = len(arr)

count = 0
print(arr)
print(dep)
for i in range(dep):
    if arr[i] == "C":
        for j in range(i+1, dep):
            if arr[j] == "O":
                for k in range(j+1, dep):
                    if arr[k] == "W":
                        count+=1
                        # print(f"{i} {j} {k}")

print(count)