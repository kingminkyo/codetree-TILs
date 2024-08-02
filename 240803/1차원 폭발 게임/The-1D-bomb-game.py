n, m = tuple(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))

while True:
    key = False
    for i in range(len(arr)-1):
        
        

        cnt = 1

        if arr[i] == arr[i+1]:
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    cnt += 1 
                
                else:
                    break

        if cnt >= m:
            key = True
            for j in range(i, i+cnt):
                arr[j] = 0

    arr = list(filter(lambda x: x>0, arr))
    # print(arr, cnt)
    if key == False:
        break

if len(arr) == 0 or m == 1:
    print(0)
else:
    print(len(arr))
    for a in arr:
        print(a)