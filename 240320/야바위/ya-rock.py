n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]

abc = [0, 0, 0]
result = 0



for i in range(3):
    abc[i] = 1
    score = 0
    for j in range(n):
        # print(abc)
        temp = abc[arr[j][0]-1]
        abc[arr[j][0]-1] = abc[arr[j][1]-1]
        abc[arr[j][1]-1] = temp

        if abc[arr[j][2]-1] == 1:
            score+=1

        # print(score)

    result = max(score, result)
    abc[i] = 0

print(result)