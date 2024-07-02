n, m, k = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def p_print():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


def rotate():
    temp = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[n - j - 1][i]
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]

def bomb():
    
    while True:
        is_bomb = False

        for i in range(n):

            for idx in range(n):
                start = idx

                end = 0

                if arr[idx][i] == 0:
                    continue
                
                for e in range(start+1, n):
                    if arr[idx][i] == arr[e][i]:
                        end += 1
                    else:
                        break
                if end>=(m-1):
                    is_bomb = True
                    for e in range(start, start+end+1):
                        arr[e][i] = 0
        if not is_bomb:
            break

                    

def rain():
    for i in range(n):
        temp = [ 0 for _ in range(n) ]
        idx = 0
        
        for j in range(n-1, -1, -1):
            if arr[j][i] != 0:
                temp[idx] = arr[j][i]
                idx += 1

        for j in range(n-1, -1, -1):
            arr[j][i] = temp[n-j-1]
            



# bomb()
for _ in range(k):
    bomb()  
    rain()
    rotate()
    rain()
    bomb()
    rain()

result = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]>0:
            result+=1
print(result)