n, m = tuple(map(int, input().split()))

arr = []

for _ in range(n):
    arr.append(int(input()))



while True:
    is_bomb = False

    for index, number in enumerate(arr):

        if number == 0:
            continue

        end_idx = index

        # print("oo",index, end_idx)

        for i in range(index+1, len(arr)):
            if arr[i] == arr[index]:
                end_idx += 1

                # print("o", end_idx)

            else:
                break
        if (end_idx - index +1 ) >= m:
            is_bomb = True        
            for i in range(index, end_idx+1):
                arr[i] = 0
        
    arr = list(filter(lambda x: x>0, arr))

    # print(arr)

    if not is_bomb:
        break


print(len(arr))
for a in arr:
    print(a, end="\n")