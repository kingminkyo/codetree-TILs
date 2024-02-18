a = int(input())
def yes(n):
    return ((n % 2) == 0) and ( ((int(n/10) + n%10) % 5 )== 0)




if yes(a):
    print("Yes")
else:
    print("No")