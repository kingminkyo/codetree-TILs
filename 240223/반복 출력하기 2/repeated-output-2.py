num = int(input())
def Hello(n):
    if n == 0:
        return
    
    print("HelloWorld")
    n-=1
    Hello(n)


Hello(num)