num = int(input())

def jegob_sum(n):
    if n<10:
        return n*n

    return jegob_sum(n//10)+((n%10)*(n%10))


print(jegob_sum(num))