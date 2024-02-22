a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = a[1]
result = 0 
result+=b[m-1]
while(m != 1):
    # print(m)
    


    if m%2 == 0:
        m//=2
    else:
        m-=1
    
    result+=b[m-1]



print (result)