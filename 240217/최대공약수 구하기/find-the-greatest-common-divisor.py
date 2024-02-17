# a, b = input().split()

# if a>=b:
#     real = a; # 12, 18인 경우 18 
# else:
#     real = b; 

# for i in real:
#     if (real%i == 0) and (b%i == 0):
#         real_num = i


# print(real_num)


a, b = map(int, input().split())  # 입력 값을 정수로 변환

def gcd(x, y):
    while(y):
        x, y = y, x % y # 12, 18인 경우 y = 18, x 12를 18로 
    return x

real_num = gcd(a, b)  # gcd 함수를 사용하여 최대공약수를 계산

print(real_num)