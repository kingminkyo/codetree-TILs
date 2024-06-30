n, m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def make_square(x1, y1, x2, y2):

    result = 0

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if arr[i][j] < 0:
                return 0
            
            result += arr[i][j]

    return result







result = 0
max_size = 0
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                if result < make_square(i, j, k, l):
                    result = make_square(i, j, k, l)
                    max_size = (k - i +1) * (l - j +1)

print(max_size)