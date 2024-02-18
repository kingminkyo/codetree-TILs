a, b, c = tuple(map(int, input().split()))


def func(*arg):
    result = 0 
    for i in arg:
        if result > i:
            result = i 
    
    return result 

print(func(a, b, c))