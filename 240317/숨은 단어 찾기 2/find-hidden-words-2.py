n, m = tuple(map(int, input().split()))
arr = [input() for _ in range(n)]

count = 0 

for i in range(n):
    for j in range(m):
        if arr[i][j] =="L":
            if n > 3:

                if i < n-3 and j < n-3 and arr[i+1][j+1] == "E" and arr[i+2][j+2] == "E" : count+=1; 
                if i < n-3 and j>=2 and arr[i+1][j-1] == "E" and arr[i+2][j-2] == "E" : count+=1; 
                if i >=2 and j>=2 and arr[i-1][j-1] == "E" and arr[i-2][j-2] == "E" : count+=1 ; 
                if i >= 2 and j < n-3 and arr[i-1][j+1] == "E" and arr[i-2][j+2] == "E" : count+=1;

                if i < n-3 and arr[i+1][j] == "E" and arr[i+2][j] == "E" : count+=1 ; 
                if i >= 2  and arr[i-1][j] == "E" and arr[i-2][j] == "E" : count+=1; 
            if m > 3:

                if j >= 2 and arr[i][j-1] == "E" and arr[i][j-2] == "E" : count+=1 ; 
                if j < n-3 and arr[i][j+1] == "E" and arr[i][j+2] == "E" : count+=1 ; 
                
        



print(count)