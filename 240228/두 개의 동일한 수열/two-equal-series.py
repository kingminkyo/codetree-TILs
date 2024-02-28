n = int(input())
aa = list(map(int,input().split()))
ab = list(map(int,input().split()))

aa.sort()
ab.sort()

if aa == ab:
    print("Yes")
else:
    print("No")