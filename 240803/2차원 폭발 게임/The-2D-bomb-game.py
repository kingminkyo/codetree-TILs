n, m, k = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def rotate():
    for i in range(n):
        for j in range(n):
            temp_arr[i][j] = arr[n - j - 1][i]

    for i in range(n):
        for j in range(n):
            arr[i][j] = temp_arr[i][j]

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n 

def arrange():
    for i in range(n):
        temp = [0 for _ in range(n)]
        cnt = 0
            
        for j in range(n-1, -1, -1):
            if arr[j][i] != 0:
                temp[cnt] = arr[j][i]
                cnt += 1 
        cnt = 0

        for j in range(n-1, -1, -1):
            arr[j][i] = temp[cnt]
            cnt += 1 


def bomb():

    while True:
        key = False
        for i in range(n):
            cnt = 1
            for j in range(n-1):
                cnt = 1
                if arr[j][i] == arr[j+1][i] and arr[j][i] != 0:
                    for k in range(j+1, n):
                        if arr[j][i] == arr[k][i]:
                            cnt += 1
                        else:
                            break
                if cnt >= m:
                    
                    for k in range(j, j+cnt):
                        if in_range(k, i):
                            arr[k][i] = 0
                            

        arrange()
        if key == False:
            break
        
        

            

    

for _ in range(k):
    bomb() 

    rotate()
    arrange()
    # print_arr()

result = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            result += 1 
if n == 1:
    if n >= m:
        print(0)
    else:
        print(1)

else:
    print(result)