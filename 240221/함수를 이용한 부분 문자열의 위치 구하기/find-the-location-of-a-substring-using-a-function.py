a = input()
b = input()

def is_same(a, b):
    for i in range(len(a)-len(b)+1):
        count = 0
        for j in range(len(b)):
            if a[i+j] == b[j]:
                count += 1
            if count == len(b):
                return i

    return -1

print(is_same(a, b))