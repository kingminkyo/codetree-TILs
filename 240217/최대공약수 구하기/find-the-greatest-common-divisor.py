a, b = input().split()

if a>=b:
    real = a; # 12, 18인 경우 18 
else:
    real = b; 

for i in real:
    if (real%i == 0) and (b%i == 0):
        real_num = i


print(real_num)