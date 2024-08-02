n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def make_rec(x1, y1, x2, y2):

    result = 0

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            result += arr[i][j]

            if arr[i][j] <= 0:
                return -1

    return result

final = -1
rec_size = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if make_rec(i, j, k, l) > 0:
                    rec_size = (k-i+1) * (l-j+1)
                if rec_size > final:
                    final = rec_size

print(final)