num = int(input())

def total_sum(n):
    if n == 0:
        return 0

    return (total_sum(n-1)+n)

print(total_sum(num))