n1, n2 = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def isSq(a, b, n1, n2):
    for i in range (n1):
        for j in range (n2):
            if a[i+j] == b[j]:
                
                print(b)
                return True
        
    return False

if isSq(a, b, n1, n2):
    print("Yes")
else:
    print("No")